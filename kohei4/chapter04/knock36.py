# coding: utf-8

# final_list[st_list[word_dic{}]]
# mecab [0:surface][1:pos][2:pos1][3:pos2]
#[4:pos3][5:活用形][6:活用型][7:base][8:発音][9:発音/n]
from collections import defaultdict

final_list = []
st_list = []

with open('./neko.txt.mecab','r') as mcb:
    for line in mcb:

        if line == 'EOS\n':
            #print(st_list)
            final_list.append(st_list)
            st_list = []
            continue

        line_l = line.replace('\t', ',').split(',')

        #with open('./neko_mecablist.txt','a') as debug:
        #    print(line_l, file = debug)

        word_dic = {}
        word_dic['surface'] = line_l[0]
        word_dic['base'] = line_l[7]
        word_dic['pos']  = line_l[1]
        word_dic['pos1'] = line_l[2]

        #print(word_dic)

        st_list.append(word_dic)

# final_list[st_list[word_dic{surface:base:pos:pos1}]]
wd_dict = defaultdict(lambda: 0)

for st_l in final_list:
    if len(st_l) > 1:
        for i in range(len(st_l)):
            word = st_l[i]['surface']
            #print(word)
            if wd_dict[word]:
                cnt = wd_dict[word]
                cnt += 1
                wd_dict[word] = cnt
            else:
                wd_dict[word] = 1


wd_dict_l = list(wd_dict.items())

wd_dict_l.sort(reverse=True, key=lambda freq: freq[1])

for i in range(10):
    print(wd_dict_l[i])






#meishi_rensetu_l.sort(reverse=True)
#meishi_rensetu_l.sort(reverse=True, key=lambda freq: freq[0])
