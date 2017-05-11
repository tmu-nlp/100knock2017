import json
import requests
from knock28 import EnglandContent
flag = EnglandContent().getItem()["国旗画像"]
url = 'https://ja.wikipedia.org/w/api.php?action=query&titles=Image:{}&prop=imageinfo&format=json&iiprop=url'.format(flag)
json_data = requests.get(url).json()
for k , v in json_data["query"]["pages"]["-1"].items():
    if k == "imageinfo":
        if len(v) > 0:
            for x, y in v[0].items():
                if x == "url":
                    print(y)
