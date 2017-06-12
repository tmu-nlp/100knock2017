"""
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号が iとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を
"->"で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示

上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y

"""

# coding: utf-8
#from collections import defaultdict
import re
import pydot

begin = 7
end =7


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

    def chome_meishi_hyousou(self, chome, dst=False):

        result = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                if morph.pos == '名詞':
                    result += chome
                    if dst:
                        return result
                    chome = ''
                else:
                    result += morph.surface
        return result




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


'以下、「素人の言語処理100本ノック」さんに頼ってます'

with open('49result.txt','w') as result:
    for ii, chunks in enumerate(neco_lines()):
        if (ii >= begin) and (ii <= end) :
            print('我輩は猫である。　第'+str(ii+1)+'行',file=result)
            noun_index_list_in_chunk = [i for i in range(len(chunks))\
                if len(chunks[i].get_morphs_pos('名詞')) > 0]
            '名詞を含むChunkのIndexList 内包表現で'
            #print('名詞INDEX',noun_index_list_in_chunk)

            if len(noun_index_list_in_chunk) < 2:
                '一個ならペアにならない'
                continue

            for i, index_x in enumerate(noun_index_list_in_chunk[:-1]):
                for index_y in noun_index_list_in_chunk[i + 1:]:
                    'x y 探しのための2重ループ、[0] to [-1] と、[i+1:] '

                    meet_y = False
                    'Flag for meet Y'
                    index_dup = -1
                    'Y字路のIndex'
                    routes_x = set()
                    'Xの道のindex集合作成'
                    'XがYに素直にdstを追って出会うまで探す'
                    dst = chunks[index_x].dst
                    'xのdst'
                    while dst != -1:
                            'DSTが最後の句でなきゃ'
                            'xのdst(dst(dst)...)とyが繋がる？'
                            if dst == index_y:
                                meet_y = True
                                break
                            '保存'
                            routes_x.add(dst)
                            dst = chunks[dst].dst
                            #print('x',index_x,'routes_x',routes_x)
                            '次のdst'


                    'xとyが繋がらなかった時'
                    if not meet_y:
                        dst = chunks[index_y].dst
                        while dst != -1:
                            'yのDSTがXの道にあれば、覚える'
                            if dst in routes_x:
                                #print(index_y,'Y_dst',dst,'routes_x',routes_x)
                                index_dup = dst
                                #print("x route meet Y route",dst)
                                break
                            else:

                                dst = chunks[dst].dst
                                'ないので、Y_inidexの次の次の(次の..)DST'

                    'Xindexは固定で、あるYindexへの道を探してあとに結果を使って出力'
                    if index_dup == -1:

                        'Y字路が無ければ'
                        print(chunks[index_x].chome_meishi_hyousou('X'),end ='',file=result)
                        dst = chunks[index_x].dst
                        while dst != -1:
                            if dst == index_y:
                                print(' -> ' + chunks[dst].chome_meishi_hyousou('Y',True),end='',file=result)
                                'Trueは模範回答合わせ？最後のYでも表層表示のときはFalse'
                                break
                            else:
                                print(' -> ' + chunks[dst].sani_surface(),end='',file=result)
                                'たどり着くまでPrecheck信じて、dstを繋ぐ'
                            dst = chunks[dst].dst
                        print(file=result)
                        'RTN出してお終い。'
                    else:

                        'Y分岐があった、index_xに入れたぞ'
                        print(chunks[index_x].chome_meishi_hyousou('X'),end='',file=result)
                        dst = chunks[index_x].dst
                        while dst != index_dup:
                            'index_dupまでdstを繋ぐ'
                            print(' -> '+ chunks[dst].sani_surface(),end='',file=result)
                            dst = chunks[dst].dst

                            'index_dupの前に、｜をだす'
                        print(' | ',end='',file=result)

                        'index_yから、index_upまで道探し'
                        print(chunks[index_y].chome_meishi_hyousou('Y'),end='',file=result)
                        dst = chunks[index_y].dst
                        while dst != index_dup:
                            print(' -> ' +chunks[dst].sani_surface(),end='',file=result)
                            dst = chunks[dst].dst
                        print(' | ',end='',file=result)
                        '|を出して、分岐点を出力'
                        print(chunks[index_dup].sani_surface(),file=result )
                        'end=''がないので、RTNが出ておしまい'

            print(file=result)
