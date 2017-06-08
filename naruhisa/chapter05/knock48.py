from knock41 import func2
from knock41 import Chunk
from collections import defaultdict

count = 0
for x in func2():
    count += 1
    relation = dict()
    SURFACE = list()
    tmp = ''
    rela_n = defaultdict(lambda: False)
    for line in x:
        for morphs in line.morphs:
            if morphs.pos == '名詞':
                rela_n[line.index] = True
            if(morphs.pos != '記号'):
                tmp += morphs.surface

        SURFACE.append(tmp)
        tmp = ''
        relation[line.index] = line.dst
    for k, v in sorted(relation.items(), key = lambda x:x[0]):
        if v != '-1' and count == 8 and rela_n[k]:
            print(SURFACE[int(k)] + ' -> ' + SURFACE[int(relation[k])], end = '')
            while(1):
                k = relation[k]
                if relation[k] == '-1':
                    break
                print(' -> ' + SURFACE[int(relation[k])], end = '')
            print()
