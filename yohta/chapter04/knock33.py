from knock30 import map_make
from knock30 import list_make

with open('../data/neko.txt.mecab','r') as f:
    noun_list = list_make(f)
    for line in noun_list:
        for word in line:
            if word['pos1'] == 'サ変接続' and word['pos'] == '名詞':
                print(word['base'])
