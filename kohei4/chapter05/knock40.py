# coding: utf-8
#from collections import defaultdict
#40. 係り受け解析結果の読み込み（形態素）
#形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
#さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

class Morph:
    def __init__(self, surface, base, pos, pos1 ):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1



f_morph_list = []
st_morph_list = []

with open('./neko.txt.cabocha','r') as mcb:
    for line in mcb:
        #line = mcb.readline()
        #print(line)
        if line == 'EOS\n':
            #print(st_morph_list)
            ##if len(st_morph_list) > 0:
                f_morph_list.append(st_morph_list)
                st_morph_list = []
                continue
            #print(st_morth_list)
            ##continue

        elif line[0] == '*' :
            continue

        else:
            #print(st_morph_list)
            line_l = line.replace('\t', ',').split(',')

        #with open('./neko_mecablist.txt','a') as debug:
        #    print(line_l, file = debug)
        # print(line_l)
            morph_here = Morph(line_l[0],line_l[7],line_l[1],line_l[2])
            st_morph_list.append(morph_here)
            #print(st_morph_list)



#print(f_morph_list[1])
    for morph in f_morph_list[2]:
        print('表層形:{}\t基本形:{}\t品詞:{}\t品詞細分類:{}'.format(morph.surface,morph.base,morph.pos, morph.pos1))
