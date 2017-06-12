"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）
を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は
「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，
次のような出力になるはずである．

始める  で
見る    は を

"""

# coding: utf-8
#from collections import defaultdict
import re
import pydot

begin = 0
end = 10


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




with open('45result.txt','w') as result:
    for ii, chunks in enumerate(neco_lines()):
        #if (ii >= begin) and (ii <= end) :
            for chunk in chunks:
                verbs = chunk.get_morphs_pos('動詞')
                #print(len(verbs))
                if len(verbs) < 1:
                    continue

                jyosi = []
                for src in chunk.srcs:
                    jyosi_in_chunk = chunks[src].get_morphs_pos('助詞')
                    if len(jyosi_in_chunk) > 1:
                        kaku_jyosi = chunks[src].get_morphs_pos('助詞','格助詞')
                        if len(kaku_jyosi) > 0:
                            jyosi_in_chunk = kaku_jyosi

                    if len(jyosi_in_chunk) > 0:
                        jyosi.append(jyosi_in_chunk[-1])

                if len(jyosi) < 1:
                    continue

                #result.write("{}\t{}\n".format(verbs[0].base,
                #' '.join(sorted(jyos.surface for jyos in jyosi))))
                'leftest verve ?'
                print("{}\t{}".format(verbs[0].base,
                ' '.join(sorted(jyos.surface for jyos in jyosi))),file=result)
