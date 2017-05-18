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
    nord_1 = re.search(r'==',words)
    nord_2 = re.search(r'===',words)
    nord_3 = re.search(r'====',words)
    words = words.strip('=')
    if len(words) > 0:
        if nord_1 and nord_2 and nord_3:
            words = words.strip('[]*|')
            print('3\t' + words)
        elif nord_1 and nord_2:
            words = words.strip('[]*|')
            print('2\t' + words)
        elif nord_1:
            words = words.strip('[]*|')
            print('1\t' + words)
