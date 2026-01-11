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
    "authorization": f"Basic {token}",
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

with open("response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
