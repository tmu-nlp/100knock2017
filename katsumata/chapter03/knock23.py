import json
import gzip
import re
from collections import defaultdict
contents = list()
section_name = defaultdict(lambda: 0)
#category_name = list()
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj.get('title') == 'イギリス':
            for text in obj['text'].split():
                contents.append(text)
for word in contents:
    matchObj_l1 = re.search(r'==.*==', word)
    if matchObj_l1:
        #matchObj_l3 = re.search(r'====.*====', word)
        s_name = re.sub(r'=', '', word)
        section_name[s_name] += 1
        print (matchObj_l1.group())
        matchObj_l2 = re.search(r'===.*===', matchObj_l1.group())
        if matchObj_l2:
            section_name[s_name] += 1
            matchObj_l3 = re.search(r'====.*====', matchObj_l1.group())
            if matchObj_l3:
                section_name[s_name] += 1

for name,value in section_name.items():
    print (name,value)
