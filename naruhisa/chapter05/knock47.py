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
        phase = 0
        phase_tmp = ''
        for morphs in line.morphs:
            if(count == 597):
                print(morphs.surface, end = ' ')
                print(morphs.pos, morphs.pos1)
            if morphs.pos1 == 'サ変接続':
                phase = 1
                phase_tmp += morphs.surface
            elif morphs.pos == '助詞':
                tmp_pp.append(morphs.surface)
                if phase == 1:
                    phase_tmp += morphs.surface
                    phase = 2
                else:
                    phase = 0
            elif(morphs.pos == '動詞' and tmp_v == '' and phase == 2):
                phase_tmp += morphs.base
                tmp_v = phase_tmp
                phase = 0
            else:
                phase = 0

            if(morphs.pos != '記号'):
                tmp_s += morphs.surface

            if(morphs.pos == '助詞'):
                rela_p[line.index] = True
            elif(morphs.pos == '動詞'):
                rela_v[line.index] = True

        PP.append(' '.join(tmp_pp))
        VERB.append(tmp_v)
        SURFACE.append(tmp_s)
        tmp_v = ''
        tmp_pp = list()
        tmp_s = ''
        relation[line.index] = line.dst
    for v in sorted(set(relation.values()), key = lambda x:x[0]):
        if v != '-1' and VERB[int(v)] != '' and count == 597:
            print(SURFACE)
            print(VERB[int(v)] + '\t', end = '')
            tmp_a = list()
            tmp_b = list()
            tmp2 = dict()
            for k in sorted(relation.keys(), key = lambda x:x[0]):
                if(relation[k]):
                    if v == relation[k] and VERB[int(v)] != '' and rela_p[k]:
                        print(k, v)
                        tmp2[PP[int(k)]] = SURFACE[int(k)]
            for k2, v2 in sorted(tmp2.items(), key = lambda x:x[0]):
                tmp_a.append(k2)
                tmp_b.append(v2)
            print(' '.join(tmp_a) + '\t' + ' '.join(tmp_b))
