from knock20 import wiki_UK
import re

my_dict = dict()

flag = 0

pattern = re.compile(r'\|(?P<key>.+?)=(?P<value>.+)')
#?P<名前>で引き出す場所？
# (?P<name>...)
# 正規表現の丸括弧に似ていますが、グループによってマッチした部分文字列は
# シンボリックグループ名 name によってアクセス可能になります。
# グループ名は有効な Python 識別子でなければならず、
# グループ名は 1 個の正規表現内で一意でなければなりません。
# シンボリックグループは番号付けもされており、番号によるアクセスも可能です。



for line in wiki_UK().split('\n'):
    if line.startswith('{{基礎情報'):
        flag = 1
    elif flag == 1 and line.startswith('}}'):
        break
    elif flag == 1:
        obj = re.search(pattern, line)
        if obj:
            my_dict[obj.group("key")] = obj.group("value")

for key, value in my_dict.items():
    print("{} {}".format(key, value))
