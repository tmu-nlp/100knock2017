from knock41 import func2
from knock41 import Chunk
from collections import defaultdict

for x in func2():
    relation = dict()
    SURFACE = list()
    tmp = ''
    rela_n = defaultdict(lambda: False)
    rela_v = defaultdict(lambda: False)
    for line in x:
        for morphs in line.morphs:
            if(morphs.pos != '記号'):
                tmp += morphs.surface
            if(morphs.pos == '名詞'):
                rela_n[line.index] = True
            elif(morphs.pos == '動詞'):
                rela_v[line.index] = True

        SURFACE.append(tmp)
        tmp = ''
        relation[line.index] = line.dst
    for k, v in sorted(relation.items(), key = lambda x:x[0]):
        if v != '-1':
            if rela_n[k] and rela_v[v]:
                print(SURFACE[int(k)] + '\t' + SURFACE[int(v)])
