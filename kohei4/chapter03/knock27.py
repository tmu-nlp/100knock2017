# coding: utf-8
#from collections import defaultdict
import re
json_dic = dict()
item_dic = dict()
kiso_dic = dict()
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

found = 0
for line in about_england.splitlines():
    if found:
        m = re.search(r'(^}}$)', line)
        if m:
            break

        m = re.search(r'(^\|)(.*)( = )(.*$)', line)

        if m:
            #print(m.groups())
            mm = re.sub(r'(\'{2,3}|\[\[|\]\])','', m.groups()[3])
            mm = re.sub(r'(\w*?\|)','',mm)
            mm = re.sub(r'(連合法 \(\d{4}年\))','',mm)

            #mm = re.sub(r'(\w*\|)','',mm)


            #mm = re.sub(r'(\'{2,3}|.*?\[\[.*?\||\[\[|\]\])','', m.groups()[3])


            #mm = re.sub(r'(\'*)','', m.groups()[3])

            kiso_dic[m.groups()[1]]=mm
            rem = m.groups()[1]
            continue

        m = re.search(r'(^\**.*>$)', line)
        #print(line)
        if m:
            #print(m.groups())
            #print(rem)
            mm = re.sub(r'(\[\[|\]\])','',m.groups()[0])
            n = kiso_dic[rem] + "\n" + mm
            kiso_dic[rem] = n


    else:
        m = re.search(r'(\{\{基礎情報.*)',line)
        #m = re.search(r'(\{\{基礎情報.*)(\|.*)( = )(.*$)',line)
        #print(m)
        if m:
            found = 1

for fields, value in kiso_dic.items():
    print(fields, "  ", value)
    #    print(mgroup()[2],mgroup()[4])
