from knock30 import map_make
from knock30 import list_make

with open('../data/neko.txt.mecab','r') as f:
    verb_list = list_make(f)
    for line in verb_list:
        for word in line:
            if word['pos'] == '動詞':
                print(word['surface'])
