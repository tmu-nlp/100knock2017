# coding: utf-8

# final_list[st_list[word_dic{}]]
# mecab [0:surface][1:pos][2:pos1][3:pos2]
#[4:pos3][5:活用形][6:活用型][7:base][8:発音][9:発音/n]


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
verb_l = []
for st_l in final_list:
    for w_dic in st_l:
        #print(w_dic)
        if w_dic['pos'] == '動詞':
                verb_l.append(w_dic['base'])

verb_set = set(verb_l)
print(verb_set)
