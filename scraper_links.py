import requests
import json
import pandas as pd


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
    "authorization": "Basic VTAwMDAzMzI5ODI6UFdfMWE5NjU5MGVjNGJjYjYwOGZmNjJjN2I0MjhlNGM5ZDc0",
}


text_data = []

n = 1
for link in urls:
    payload = {"url": link, "headless": "html"}
    print(link)
    text_data.append(link)

    # response = requests.post(url, json=payload, headers=headers)
#
# text_data.append({"link": link, "text": response.text})
# n += 1
# if n == 20:
#    break
print(text_data)
# df = pd.DataFrame(text_data)
# df.to_excel("scraped_links_text.xlsx", index=False)
# print(df)
#
