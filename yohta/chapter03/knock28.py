import json
import gzip
import re

text = []
dict1 = {}

f = gzip.open('jawiki-country.json.gz','r')
for line in f:
    line = json.loads(line.decode('utf-8'))
    #line = json.loads(line,"utf-8"),
    if line.get('title') == 'イギリス':
        for context in line['text'].split('\n'):
            text.append(context)

for line in text:
    nord = re.search(r'{{基礎情報',line)
    nord_1 = re.search(r'^\|',line)
    end = re.match(r'}}',line)
    if end:
        break
    if nord_1:
        word = re.sub(r'^\|\*','',line)
        word = re.sub(r'\'','',word)
        word = re.sub(r'\[\[','',word)
        word = re.sub(r'\]\]','',word)
        word = re.sub(r'\[http.*\]','',word)
        word = re.sub(r'\<ref.*\>','',word)
        word = re.sub(r'\<br.*\>','',word)
        word = re.split(r'\s\=\s',word)
        dict1[word[0]] = word[1]

for key,bar in sorted(dict1.items()):

    print('{}{}:{}{}'.format(key,'\t','\t',bar))
