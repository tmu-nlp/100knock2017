import json
import gzip
import re
contents = list()
category_name = list()
c = 'Category'
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj.get('title') == 'イギリス':
            for text in obj['text'].split():
                contents.append(text)
for word in contents:
    matchObj = re.search(r'Category', word)
    if matchObj:
        #category_name.append(word[matchObj.end()+1:len(word)-2])
        c_name = re.search(r'([ぁ-ん ァ-ン]|[一-龥]).*([ぁ-ん ァ-ン]|[一-龥])',word)
        category_name.append(c_name.group())

for name in category_name:
    print (name)
