import requests
import json
import login


token = login.token


def collect_data(search_by: str, page_from: int = 1, page_count: int = 10):
    url = "https://scraper-api.decodo.com/v2/scrape"

    payload = {
        "target": "google_search",
        "query": search_by,
        "headless": "html",
        "locale": "lt-lt",
        "geo": "Lithuania",
        "page_from": page_from,
        "google_results_language": "en",
        "parse": True,
        "page_count": page_count,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Basic {token}",
    }

    print(f"Scraping Google for '{search_by}'", flush=True)
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    #
    print("Scraping completed. Saving response to file.")
    with open(
        f"./output/google_output/response_{search_by}_{page_from}_{page_count}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Response saved successfully.")


if __name__ == "__main__":
    collect_data("test", 1, 1)
