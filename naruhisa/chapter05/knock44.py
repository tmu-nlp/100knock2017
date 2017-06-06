from knock41 import func2
from knock41 import Chunk

for i, x in enumerate(func2()):
    with open('GRAPH/graph{}.dot' .format(i), 'w') as f:
        f.write('digraph g{\n')
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
                f.write('\"' + SURFACE[int(k)] + '\"' + '->' + '\"' + SURFACE[int(v)] + '\"\n')
        f.write('}')

# dot -T png graph7.dot -o graph7.out.png
