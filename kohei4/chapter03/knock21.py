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


for line in about_england.splitlines():
    result = re.search('Category',line)
    #print(line)
    if result:
       print(line)
#        print(*line)
