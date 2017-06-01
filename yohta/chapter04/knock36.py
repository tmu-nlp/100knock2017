from knock30 import map_make
from knock30 import list_make
from collections import defaultdict

with open('../data/neko.txt.mecab','r') as f:
    sent_list = list_make(f)
    word_list = []
    word_list_counter = defaultdict(lambda: 0)
#    counter = 0
    for i in range(0,len(sent_list)):
        for j in range(0,len(sent_list[i])):
#        for word1,word2 in line.items():
#            if not sent_list[i][j]['surface'] in word_list:
#                word_list_counter[sent_list[i][j]['surface']] = 1
#                word_list.append(sent_list[i][j]['surface'])
#            else:
            word_list_counter[sent_list[i][j]['surface']] += 1
    for w,c in sorted(word_list_counter.items(), key = lambda x:x[1], reverse = True):
        print('{}:{}'.format(w,c))
