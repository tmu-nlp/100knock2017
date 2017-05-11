import json
import gzip
with gzip.open('jawiki-country.json.gz') as f:
    for line in f:
        data = json.loads(line.decode("utf-8"))
        if data ['title']=='イギリス': 
            print(data['text'])
