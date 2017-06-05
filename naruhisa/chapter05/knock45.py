from knock41 import func2
from knock41 import Chunk
from collections import defaultdict
count = 0
for x in func2():
    count += 1
    relation = dict()
    PP = list()
    VERB = list()
    tmp_pp = list()
    tmp_v = ''

    rela_p = defaultdict(lambda: False)
    rela_v = defaultdict(lambda: False)
    for line in x:
        for morphs in line.morphs:
            if(morphs.pos == '助詞' and morphs.pos != '記号'):
                tmp_pp.append(morphs.surface)
            elif(morphs.pos == '動詞' and morphs.pos != '記号' and tmp_v == ''):
                tmp_v = morphs.base
            if(morphs.pos == '助詞'):
                rela_p[line.index] = True
            elif(morphs.pos == '動詞'):
                rela_v[line.index] = True
        tmp_pp = tmp_pp
        PP.append(' '.join(tmp_pp))
        VERB.append(tmp_v)
        tmp_v = ''
        tmp_pp = list()
        relation[line.index] = line.dst
    for v in sorted(set(relation.values()), key = lambda x:x[0]):
        if v != '-1' and VERB[int(v)] != '' and count == 8:
            print(VERB[int(v)] + '\t', end = '')
            tmp = list()
            for k in sorted(relation.keys(), key = lambda x:x[0]):
                if(relation[k]):
                    if v == relation[k] and VERB[int(v)] != '':
                        tmp.extend(PP[int(k)].split())
            print(' '.join(sorted(tmp)))
