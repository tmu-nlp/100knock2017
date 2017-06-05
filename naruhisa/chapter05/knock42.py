from knock41 import func2
from knock41 import Chunk

for x in func2():
    relation = dict()
    SURFACE = list()
    tmp = ''
    for line in x:
        for morphs in line.morphs:
            if morphs.pos != '記号':
                tmp += morphs.surface
        SURFACE.append(tmp)
        tmp = ''
        relation[line.index] = line.dst
    for k, v in sorted(relation.items(), key = lambda x:x[0]):
        if v != '-1':
            print(SURFACE[int(k)] + '\t' + SURFACE[int(v)])
