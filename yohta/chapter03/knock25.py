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
#        word = re.split(r'\s\=\s',word)
#        word = word.replace('<ref> *</ref>','')
#        word = word.replace('<ref */>','')
#        word = word.replace('<ref> *</br>','')
#        word = word.replace('[[','')
#        word = word.replace(']]','')
        word = re.split(r'\s\=\s',word)
        dict1[word[0]] = word[1]
#        word.append('')
#        if word[1] is :
#            print('{}:{}'.format(word[0],word[1]))
#        else:
for key,bar in sorted(dict1.items()):
    print('{}{}:{}{}'.format(key,'\t','\t',bar))

#        temp = nord
#    temp = re.sub('^\|','',line)
#        l = re.split('\s\=\s',line)
#        l[1] = l[1].replace('\n','')
#        temp[l[0]] = l[1]
#        temp += line
#    for words in temp:
#        print('{}'.format(words))
