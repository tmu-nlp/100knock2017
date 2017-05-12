import json
import gzip
import re
contents = list()
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj.get('title') == 'イギリス':
            for text in obj['text'].split():
                contents.append(text)
for word in contents:
    matchObj = re.search(r'Category',word)
    if matchObj:
        print (word)
