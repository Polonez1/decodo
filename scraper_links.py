import requests
import json
import pandas as pd
import login

with open("response.json", "r", encoding="utf-8") as f:
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
df.to_excel("data.xlsx", index=False)
print(df)
