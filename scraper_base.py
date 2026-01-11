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


search_by = "homeopatija"

url = "https://scraper-api.decodo.com/v2/scrape"

payload = {
    "target": "google_search",
    "query": "homeopatija",
    "headless": "html",
    "page_from": "1",
    "google_results_language": "en",
    "parse": True,
    "page_count": 10,
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Basic {token}",
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

with open("response_10.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done")
