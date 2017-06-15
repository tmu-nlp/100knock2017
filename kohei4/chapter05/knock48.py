"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た

"""

# coding: utf-8
#from collections import defaultdict
import re
import pydot

begin = 7
end = 7


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

        if len(jyosi) > 0:
            jyosi_s = jyosi[-1].surface
            #print(jyosi_s)
            return jyosi_s

        else:
            return ''

    def get_sahen_wo(self):
        for i, morph in enumerate(self.morphs[0:-1]):
            if (morph.pos == '名詞')\
                    and (morph.pos1 == 'サ変接続')\
                    and (self.morphs[i + 1].pos == '助詞')\
                    and (self.morphs[i + 1].surface == 'を'):
                return morph.surface + self.morphs[i + 1].surface

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




with open('48result.txt','w') as result:
    for ii, chunks in enumerate(neco_lines()):
        #if (ii >= begin) and (ii <= end) :
            for chunk in chunks:
                if len(chunk.get_morphs_pos('名詞')) > 0:

                    print(chunk.sani_surface(),end=' ',file=result)
                    dst = chunk.dst

                    while True:
                        if dst == -1:
                            break

                        print('-> ' + chunks[dst].sani_surface(),end=' ',file=result)
                        dst = chunks[dst].dst
                    print(file=result)
            #print(file=result)
