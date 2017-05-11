import json
with open('jawiki-country.json') as json_data:
    lines = json_data.readlines()
    for line in lines:
        data = json.loads(line)
        if data["title"] == "イギリス":
            print(data["text"])
