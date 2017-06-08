# coding: utf-8
#from collections import defaultdict
import re
#41. 係り受け解析結果の読み込み（文節・係り受け）
#40に加えて，文節を表すクラスChunkを実装せよ．
#このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
#係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
#さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
#8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

#* 0 2D 0/1 -1.911675


class Morph:
    def __init__(self, surface, base, pos, pos1 ):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)



chunk_list = []

with open('./neko.txt.cabocha','r') as mcb:
    chunks = dict()
    idx = -1


    for line in mcb:
        #line = mcb.readline()
        #print(line)
        if line == 'EOS\n':

                if len(chunks) > 0:

                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    'order by IDX'
                    chunk_list.append(list(zip(*sorted_tuple))[1])
                    'after sort, no ID, just Class Chunk list'
                    #print(*list(zip(*sorted_tuple))[1])
                    chunks.clear()

                else:
                    chunk_list.append([])



        elif line[0] == '*' :
            'line is str'
            cabo = line.split(' ')
            'cabo is list'
            idx = int(cabo[1])
            dst = int(re.search(r'(.*?)D', cabo[2]).group(1))
            'dst is just before D'
            #print(idx)

            if idx not in chunks:
                chunks[idx] = Chunk()
            'no IDX then connect to Class through DIC'
            chunks[idx].dst = dst
            'register dst for the idx'
            if dst != -1:
                if dst not in chunks:
                    chunks[dst] = Chunk()
                chunks[dst].srcs.append(idx)
            'no chunks[dst], create and register idx as srcs'

        else:
            #print(st_morph_list)
            line_l = line.replace('\t', ',').split(',')

        #with open('./neko_mecablist.txt','a') as debug:
        #    print(line_l, file = debug)
        # print(line_l)
            chunks[idx].morphs.append(Morph(line_l[0],line_l[7],line_l[1],line_l[2]))
            'there should be chunks[idx] '
            #print(st_morph_list)



chunks = chunk_list[7]

for j, chunk in enumerate(chunks):
    print('[{}]{}'.format(j, chunk))

#print(f_morph_list[1])
