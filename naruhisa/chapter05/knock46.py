from knock41 import func2
from knock41 import Chunk
from collections import defaultdict
count = 0
for x in func2():
    count += 1
    relation = dict()
    PP = list()
    VERB = list()
    SURFACE = list()
    tmp_pp = list()
    tmp_v = ''
    tmp_s = ''



    rela_p = defaultdict(lambda: False)
    rela_v = defaultdict(lambda: False)
    for line in x:
        for morphs in line.morphs:
            if(morphs.pos == '助詞' and morphs.pos != '記号'):
                tmp_pp.append(morphs.surface)
            elif(morphs.pos == '動詞' and morphs.pos != '記号' and tmp_v == ''):
                tmp_v = morphs.base

            if(morphs.pos != '記号'):
                tmp_s += morphs.surface

            if(morphs.pos == '助詞'):
                rela_p[line.index] = True
            elif(morphs.pos == '動詞'):
                rela_v[line.index] = True
        tmp_pp = sorted(tmp_pp)
        PP.append(' '.join(tmp_pp))
        VERB.append(tmp_v)
        SURFACE.append(tmp_s)
        tmp_v = ''
        tmp_pp = list()
        tmp_s = ''
        relation[line.index] = line.dst
    for v in sorted(set(relation.values()), key = lambda x:x[0]):
        if v != '-1' and VERB[int(v)] != '' and count == 8:
            print(VERB[int(v)] + '\t', end = '')
            tmp_a = list()
            tmp_b = list()
            tmp2 = dict()
            for k in sorted(relation.keys(), key = lambda x:x[0]):
                if(relation[k]):
                    if v == relation[k] and VERB[int(v)] != '' and rela_p[k]:
                        tmp2[PP[int(k)]] = SURFACE[int(k)]
            for k2, v2 in sorted(tmp2.items(), key = lambda x:x[0]):
                tmp_a.append(k2)
                tmp_b.append(v2)
            print(' '.join(tmp_a) + '\t' + ' '.join(tmp_b))
