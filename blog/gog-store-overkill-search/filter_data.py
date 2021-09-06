import json

import requests

# Merge JSON data in a single list
data = []
for i in range(1, 13):
    with open("games" + str(i) + ".json", "r") as fp:
        tmp = json.load(fp)
        data = data + tmp["products"]

# Filter - Price <= 1.30 and Price > 0
data = [
    x
    for x in data
    if float(x["price"]["finalAmount"]) <= 1.3 and float(x["price"]["finalAmount"]) > 0
]

# Filter - Remove DLCs
gog_url = "https://www.gog.com"
DLC_flag_text = "To play this game you also need"
data = [x for x in data if DLC_flag_text not in requests.get(gog_url + x["url"]).text]

if len(data) == 0:
    print("No games in the [0.01, 1.30] price range!")
    exit

for el in data:
    print(el["title"] + "\tPrice: " + el["price"]["finalAmount"])
