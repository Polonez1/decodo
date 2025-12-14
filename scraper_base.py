import requests
import json


auth = "U0000332982"
password = "PW_1a96590ec4bcb608ff62c7b428e4c9d74"
token = "VTAwMDAzMzI5ODI6UFdfMWE5NjU5MGVjNGJjYjYwOGZmNjJjN2I0MjhlNGM5ZDc0"

url = "https://scraper-api.decodo.com/v2/scrape"
search_by = "homeopatija"

payload = {
    "target": "google",
    "url": f"https://www.google.com/search?q={search_by}&source=hp&ei=OrK3ZITEEY6Ixc8P3NemmA4&iflsig=AD69kcEAAAAAZLfASni8y8AdTBIjpShc1wPCNRMLoubj&ved=0ahUKEwiEyafav5qAAxUORPEDHdyrCeMQ4dUDCAk&uact=5&oq=pizza&gs_lp=Egdnd3Mtd2l6IgVwaXp6YTILEC4YgAQYxwEY0QMyBRAAGIAEMgUQLhiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyCxAuGIAEGMcBGK8BMgsQLhiABBjHARivATIFEC4YgARI1ApQgARYyQlwAXgAkAEAmAF1oAGuBKoBAzAuNbgBA8gBAPgBAagCAA&sclient=gws-wiz",
    "headless": "html",
    "locale": "lt-lt",
    "parse": True,
    "page_count": 10,
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic VTAwMDAzMzI5ODI6UFdfMWE5NjU5MGVjNGJjYjYwOGZmNjJjN2I0MjhlNGM5ZDc0",
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

with open("response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
