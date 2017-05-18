import json
import gzip
import re

text = []

f = gzip.open('jawiki-country.json.gz','r')
for line in f:
    line = json.loads(line.decode('utf-8'))
    #line = json.loads(line,"utf-8"),
    if line.get('title') == 'イギリス':
        for context in line['text'].split('\n'):
            text.append(context)
#text = ' '.join(text)
#print(text)
for words in text:
    nord_1 = re.search(r'File',words)
    nord_2 = re.search(r'ファイル',words)
    if nord_1 or nord_2:
        words = words.strip('[]*|')
        words = re.split('\|',words)
        print(words[0])
