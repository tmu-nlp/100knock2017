import json
import gzip
import re

text = []

f = gzip.open('jawiki-country.json.gz','r')
for line in f:
    line = json.loads(line.decode('utf-8'))
    #line = json.loads(line,"utf-8"),
    if line.get('title') == 'イギリス':
        for context in line['text'].split():
            text.append(context)
for words in text:
    nord = re.search(r'Category',words)
    if nord:
        words = words.strip('[]*|')
        print(words)
