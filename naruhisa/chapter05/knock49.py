from knock41 import func2
from knock41 import Chunk
from collections import defaultdict
count = 0
for x in func2():
    count += 1
    relation = dict()
    SURFACE = list()
    X_list = list()
    Y_list = list()
    tmp = ''
    verX = ''
    verY = ''
    rela_n = defaultdict(lambda: False)
    for line in x:
        for morphs in line.morphs:
            if(morphs.pos != '記号'):
                tmp += morphs.surface

            if(morphs.pos == '名詞'):
                rela_n[line.index] = True
                verX += 'X'
                verY += 'Y'
            elif(morphs.pos != '名詞' and morphs.pos != '記号'):
                verX += morphs.surface
                verY += morphs.surface

        X_list.append(verX)
        Y_list.append(verY)
        SURFACE.append(tmp)
        verX = ''
        verY = ''
        tmp = ''
        relation[int(line.index)] = int(line.dst)
    if count == 9958:
        phase = 0
        for i in range(len(SURFACE)):
            for j in range(i + 1, len(SURFACE)):
                collision = False
                phase += 1
                if rela_n[str(i)] and rela_n[str(j)]:
                    tmp_adr = list()
                    x = i
                    y = j
                    while y != -1:
                        y = relation[y]
                        tmp_adr.append(y)
                    while x != -1:
                        x = relation[x]
                        if x == j:
                            break
                        if x in tmp_adr:
                            collision = True
                            col_phase = x
                            break
                    print(X_list[i], end = '')
                    x = i
                    y = j
                    if collision:
                        while x != -1:
                            if relation[x] == col_phase:
                                break
                            x = relation[x]
                            print(' -> ' + SURFACE[x], end = '')

                        print(' | ' +  Y_list[y], end = '')
                        y = relation[y]
                        while 1:
                            if y == col_phase:
                                print(' | ' + SURFACE[col_phase], end = '')
                                break
                            print(' -> ' + SURFACE[y], end = '')
                            y = relation[y]
                    elif not collision:
                        while 1:
                            x = relation[x]
                            if x == j:
                                break
                            print(' -> ' + SURFACE[x], end = '')
                        print(' -> Y', end ='')
                    print()
