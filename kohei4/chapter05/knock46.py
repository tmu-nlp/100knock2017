"""
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）
をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを

"""

# coding: utf-8
#from collections import defaultdict
import re
import pydot

begin = 0
end =10


class Morph:
    def __init__(self, surface, base, pos, pos1 ):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.\
        format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):
        '''print object special function'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

    def sani_surface(self):
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号' :
                result += morph.surface
        return result

    def chk_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_morphs_pos(self, pos, pos1 = ''):
        res_l=[]
        if len(pos1) > 0:
            for res in self.morphs:
                if (res.pos == pos) and (res.pos1 == pos1):
                    res_l.append(res)
            return res_l
        else:
            for res in self.morphs:
                if res.pos == pos:
                    res_l.append(res)
            return res_l


    def get_kaku_jyosi(self):

        jyosi = self.get_morphs_pos('助詞')
        if len(jyosi) > 1:
            kaku_jyosi = self.get_morphs_pos('助詞','格助詞')
            if len(kaku_jyosi) > 0:
                jyosi = kaku_jyosi

        #print(*jyosi)
        #print()
        if len(jyosi) > 0:
            jyosi_s = jyosi[-1].surface
            #print(jyosi_s)
            return jyosi_s

        else:
            return ''

def neco_lines():

    with open('./neko.txt.cabocha','r') as mcb :

        chunks = dict()
        idx = -1


        for line in mcb:
            #line = mcb.readline()
            #print(line)
            if line == 'EOS\n':
                    # Chunkのリストを返す
                if len(chunks) > 0:
                    #for kk, ll in chunks.items():
                    #    print(kk, ll)
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    #for kk, ll in sorted_tuple:
                    #    print(kk, ll)
                    yield (list(zip(*sorted_tuple))[1])
                    #for kk in list(zip(*sorted_tuple))[1]:
                    #    print(kk)
                    chunks.clear()

                else:
                    yield []

            elif line[0] == '*' :
                cabo = line.split(' ')
                idx = int(cabo[1])
                dst = int(re.search(r'(.*?)D', cabo[2]).group(1))
                #print(idx)
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)
            else:
                #print(st_morph_list)
                line_l = line.replace('\t', ',').split(',')

            #with open('./neko_mecablist.txt','a') as debug:
            #    print(line_l, file = debug)
            # print(line_l)
                chunks[idx].morphs.append(Morph(line_l[0],line_l[7],line_l[1],line_l[2]))
                #print(st_morph_list)
        raise StopIteration




with open('46result.txt','w') as result:
    for ii, chunks in enumerate(neco_lines()):
        #if (ii >= begin) and (ii <= end) :
            for chunk in chunks:
                verbs = chunk.get_morphs_pos('動詞')
                if len(verbs) < 1:
                    continue

                jyosi_chunks = []

                for src in chunk.srcs:
                    if len(chunks[src].get_kaku_jyosi()) > 0:
                        jyosi_chunks.append(chunks[src])
                if len(jyosi_chunks) < 1:
                    continue

                #print(*jyosi_chunks)
                #print()
                jyosi_chunks.sort(key=lambda x: x.get_kaku_jyosi())

                print("{}\t{}\t{}\n".format(verbs[0].base,
                ' '.join([chunk.get_kaku_jyosi() for chunk in jyosi_chunks ]),
                ' '.join([chunk.sani_surface() for chunk in jyosi_chunks] ))
                ,file = result)
