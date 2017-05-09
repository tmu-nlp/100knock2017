import gzip
import json

def gen_uk_info():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for w in f:
            jsonObj = json.loads(w)
            if jsonObj['title'] == 'イギリス':
                # print(jsonObj['text'])
                return jsonObj['text']
