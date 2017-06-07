from knock40 import Morph
from knock41 import func41,Chunk

N = 10
counter = 0
"""
for line in func41():
    if counter > N:
        break
    for b in line:
        dst = b.getDst()
        nouns = list()
        if b.getNoun == 'True' and dst != -1:
#            continue
            nouns.append(b.getSurword())

            while dst != -1:
                nouns.append(line[dst].getSurword())
                dst = line[dst].getDst()
        print(' -> '.join(nouns))
    counter += 1
"""
for line in func41():
    if counter > N:
        break
    for b in line:
        dst = b.getDst()
        nouns = list()
        if b.getNoun is 'False' or  dst == -1:
            continue
        nouns.append(b.getSurword())

        while dst != -1:
            nouns.append(line[dst].getSurword())
            dst = line[dst].getDst()
        print(' -> '.join(nouns))
    counter += 1
