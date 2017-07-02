#!usr/bin/python

import bz2
import random


fin = "./data/enwiki_knock81.txt.bz2"
fout = "./data/pair_knock82.txt"


print("Loading file....", end=" ", flush=True)
corpus = bz2.decompress(open(fin, "rb").read()).decode().split()
print("done")


print('write file', end=" ", flush=True)
fout = open(fout, "w")
for num in range(5, len(corpus) - 5):
  rand_int = random.randint(1, 5)
  fout.write("{}\t{}\n".format(corpus[num],
    '\t'.join([corpus[i] for i in range(num-rand_int, num+rand_int+1) if num != i])))


fout.close()
print("done")
