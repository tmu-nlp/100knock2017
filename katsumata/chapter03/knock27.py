import json
import gzip
import re
contents = list() #イギリス記事（改行区切り）
flag_base = 0
#イギリスの読み込み
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj.get('title') == 'イギリス':
            for text in obj['text'].split('\n'):
                contents.append(text)

dict_base = dict()
#辞書に基本情報を入れる
for word in contents:
    matchObj = re.search(r'{{基礎情報.*',word)
    finishObj = re.match(r'}}', word)
    if finishObj:
        break
    if flag_base == 1:
        equalObj = re.search(r'=', word)
        if equalObj:   
            temp_str = ''
            equal_place = equalObj.start()
            temp_str += word[equal_place+1:]
            field_name = word[1:equal_place-1]
        else:
            temp_str += '\n'+'\t'+word
        dict_base[field_name] = temp_str    
    if matchObj:
        flag_base = 1
#協調を除去する
for key, value in dict_base.items():
    enphaObj = re.search(r'\'\'\'', value)
    if enphaObj:
        dict_base[key] = re.sub(r'\'',r'', value)
#内部リンク除去        
for key,value in dict_base.items():
    """
    [[記事名|表示名]]への対応
    記事名も取っていく__
    """
    #[[.*]]
    inner_linkObj1 = re.search(r'\[+.*\]+', value)
    #[[.*|.*]]
    inner_linkObj2 = re.search(r'\[\[.*\|.*\]\]',value)
    #[[.*]].*[[.*|.*]]
    inner_linkObj3 = re.search(r'\[\[.*\]\].*\[\[.*\|.*\]\]',value)
    if inner_linkObj3:
        value = re.sub(r'(?<=\()\[.*|', r'', value)
    elif inner_linkObj2:
        value = re.sub(r'\[.*\|', r'', value)
    #ファイルの処理は除外
    fileObj = re.search(r'ファイル', value)
    #{}の処理も例外
    exceptObj = re.search(r'{{.*}}', value)
    if inner_linkObj1 and not fileObj and not exceptObj:
        dict_base[key] = re.sub(r'\[|\]|\||#',r'', value)
    elif exceptObj:
        dict_base[key] = re.sub(r'\[|\]', r'', value)
for key, value in sorted(dict_base.items()):
    print ('{} : {}'.format(key, value))
