# coding: utf-8
#from collections import defaultdict
import re

#42. 係り元と係り先の文節の表示
#係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
#ただし，句読点などの記号は出力しないようにせよ．

#* 0 2D 0/1 -1.911675


class Morph():
    def __init__(self, surface, base, pos, pos1 ):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):
        '''オブジェクトの文字列表現'''
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
                # Chunkのリストを返す
                if len(chunks) > 0:

                    #for kk, ll in chunks.items():
                    #    print(kk, ll)

                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])

                    #for kk, ll in sorted_tuple:
                    #    print(kk, ll)

                    chunk_list.append(list(zip(*sorted_tuple))[1])

                    #for kk in list(zip(*sorted_tuple))[1]:
                    #    print(kk)



                    chunks.clear()

                else:
                    chunk_list.append([])



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



for l in range(len(chunk_list)):

    chunks = chunk_list[l]

    bunsetu_l=[]
    for j, chunk in enumerate(chunks):

    #    for i in range(len(chunk.morphs)):
    #        print(chunk.morphs[i].surface)
        bunsetu = ""
        for i, k in enumerate(chunk.morphs):
            bunsetu += k.surface

        bunsetu_l.append([chunk.dst,chunk.srcs,bunsetu])
        #print(bunsetu)
        #print(chunk.srcs)
        #print(chunk.dst)

    #print(bunsetu_l)
    print("第{}文".format(l+1))

    for i, bunsetu in enumerate(bunsetu_l):
        if bunsetu[0] == -1:
            continue

        kakarimoto = re.sub(r'(。|、|」|「)','',bunsetu[2])
        kakarisaki = re.sub(r'(。|、|」|「)','',bunsetu_l[bunsetu[0]][2])
        print("{}\t{}".format(kakarimoto,kakarisaki))

    print()
