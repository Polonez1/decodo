import requests
import json
import pandas as pd
import login


def scrap_links(search_by: str, page_from: int = 1, page_count: int = 1):
    print(f"Scraping links for '{search_by}'", flush=True)
    with open(
        f"./output/google_output/response_{search_by}_{page_from}_{page_count}.json",
        "r",
        encoding="utf-8",
    ) as f:
        data = json.load(f)

    urls = []

    for block in data.get("results", []):
        organic = (
            block.get("content", {})
            .get("results", {})
            .get("results", {})
            .get("organic", [])
        )

        for item in organic:
            url = item.get("url")
            if url:
                urls.append(url)

    # ----------------------------------------------#
    url = "https://scraper-api.decodo.com/v2/scrape"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Basic {login.token}",
    }

    text_data = []
    print(f"Total URLs to scrape: {len(urls)}", flush=True)
    n = 1
    for link in urls:
        payload = {"url": link, "headless": "html"}

        response = requests.post(url, json=payload, headers=headers)
        #
        text_data.append({"link": link, "text": response.text})
        n += 1
        # if n == 20:
        #   break

    df = pd.DataFrame(text_data)
    df.to_excel(
        f"./output/excel_output/data_{search_by}_{page_from}_{page_count}.xlsx",
        index=False,
    )
    print(df.head(3))
    print("Links scraping completed and data saved to Excel.")
