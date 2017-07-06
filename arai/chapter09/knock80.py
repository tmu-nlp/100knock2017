import re
import bz2


with open('knock80.txt', 'w') as w_f:
    for line in bz2.BZ2File('enwiki-20150112-400-r100-10576.txt.bz2', 'rb'):
        corpus = []
        line = line.decode()
        word = line.strip().split()
        for token in word:
            token = re.sub('[\.,!\?;:\(\)\[\]\'\"]+',  '', token)
            if len(token) != 0:
                corpus.append(token)
        #print(corpus)
        w_f.write(' '.join(corpus) + '\n')


