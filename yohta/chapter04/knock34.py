from knock30 import map_make
from knock30 import list_make

with open('../data/neko.txt.mecab','r') as f:
    sent_list = list_make(f)
    for i in range(len(sent_list)):
        if len(sent_list[i]) >= 3:
            for j in range(1,len(sent_list[i])-1):
#        for word1,word2 in line.items():
                if sent_list[i][j-1]['pos'] == '名詞' and sent_list[i][j]['surface'] == 'の' and sent_list[i][j+1]['pos'] == '名詞':
                    print('{}{}{}'.format(sent_list[i][j-1]['surface'],sent_list[i][j]['surface'],sent_list[i][j+1]['surface']))
