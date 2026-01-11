import requests
import json
import login

# auth = "U0000341401"
# password = "PW_1fc56866964abc72a4bb95e70027b814b"
# token = "VTAwMDAzNDE0MDE6UFdfMWZjNTY4NjY5NjRhYmM3MmE0YmI5NWU3MDAyN2I4MTRi"
auth = login.auth
password = login.password
token = login.token
# patrykkonst123A#


def google_search_scrape(search_by: str, page_from: int = 1, page_count: int = 10):
    url = "https://scraper-api.decodo.com/v2/scrape"

    payload = {
        "target": "google_search",
        "query": search_by,
        "headless": "html",
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

    print(f"Scraping Google for '{search_by}'")
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    print("Scraping completed. Saving response to file.")
    with open(
        f"./output/response_{search_by}_{page_from}_{page_from}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Response saved successfully.")


if __name__ == "__main__":
    google_search_scrape("test", 1, 1)
