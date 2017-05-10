# coding: utf-8
#from collections import defaultdict
import re
json_dic = dict()
item_dic = dict()
import json

with open('jawiki-country.json','rb') as jsn:
    for line in jsn:
        json_dic = json.loads(line)
#        print([json_dic["title"]])
        item_dic[json_dic["title"]] = json_dic
        #print(item_dic[json_dic["title"]]["text"])
#        print(json_dic)

#print(item_dic)

about_england = item_dic['イギリス']['text']

category=[]
for line in about_england.splitlines():
    m = re.search(r'(.Category:)(\w+)',line)
    if m:
        category.append(m.groups()[1])

print('Categoryの中身')
for n in category:
    print(n)
#print()
#print(category)
