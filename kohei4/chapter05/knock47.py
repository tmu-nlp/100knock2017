"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を
満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン

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




with open('47result.txt','w') as result:
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

                sahen_wo = ''

                for chunk_src in jyosi_chunks:
                    sahen_wo = chunk_src.get_sahen_wo()
                    #print(sahen_wo)
                    if len(sahen_wo) > 0:
                        chunk_sub = chunk_src
                        break

                if len(sahen_wo) < 1:
                    continue

                jyosi_chunks.remove(chunk_sub)


                jyosi_chunks.sort(key=lambda x: x.get_kaku_jyosi())

                print("{}\t{}\t{}".format(
                sahen_wo + verbs[0].base,
                ' '.join([chunk.get_kaku_jyosi() for chunk in jyosi_chunks ]),
                ' '.join([chunk.sani_surface() for chunk in jyosi_chunks] ))
                ,file=result)
