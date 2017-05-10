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

m_file=[]
for line in about_england.splitlines():
    m = re.search(r'(ファイル:|File:)(.*\.\w{3})(\|.*\|?\]$)',line)
    #m = re.search(r'(^\=+)(\w+)($\=+)',line)
    if m:
        m_file.append( m.groups()[1] )
        print(m.groups()[2])

print()
print('メディアファイル')
#print(section)
for mf in m_file:
    print(mf)
print()
