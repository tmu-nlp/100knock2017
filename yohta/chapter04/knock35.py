from knock30 import map_make
from knock30 import list_make

with open('../data/neko.txt.mecab','r') as f:
    sent_list = list_make(f)
    noun_list = []
    noun_list_stock = []
    for i in range(len(sent_list)):
        for j in range(0,len(sent_list[i])):
#        for word1,word2 in line.items():
            if sent_list[i][j]['pos'] == '名詞':
                frag = 1
                noun_list_stock.append(sent_list[i][j]['surface'])
            elif frag ==1:
                frag = 0
                noun_list.append(''.join(noun_list_stock))
                noun_list_stock = []
    print(noun_list)
