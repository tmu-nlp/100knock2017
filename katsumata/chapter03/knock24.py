import json
import gzip
import re
contents = list()
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj.get('title') == 'イギリス':

            for text in obj['text'].split('\n'):
                contents.append(text)
                
#print (contents)
for word in contents:
    matchObj = re.search(r'(File|ファイル).*\....\|',word)
    if matchObj:
        f_name = (re.sub(r'\|', '', matchObj.group()))
        print (f_name)
