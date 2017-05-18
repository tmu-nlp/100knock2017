import json
import gzip

with gzip.open('jawiki-country.json.gz', 'r', 'utf-8') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if(obj['title'] == 'イギリス'):
                with open('UKdata.txt', 'w') as output:
                    output.write(obj['text'])
