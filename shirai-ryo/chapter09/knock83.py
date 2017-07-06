from collections import defaultdict
import pickle

with open("corpus82.txt") as in_text:
    f1 = open("f_tc_83", "wb")
    f2 = open("f_t_83", "wb")
    f3 = open("f_c_83", "wb")
    fN = open("N_83", "wb")

    f_tc = defaultdict(int)
    f_t = defaultdict(int)
    f_c = defaultdict(int)
    N = 0
    count = 0
    for line in in_text:
        tc = line.strip('\n').replace('\t', ' ')
        line = tc.split()
        # [t, c]の形になってる
        t = line[0]
        c = line[1]
        f_tc[tc] += 1
        f_t[t] += 1
        f_c[c] += 1
        N += 1

    pickle.dump(dict(f_tc), f1)
    pickle.dump(dict(f_t), f2)
    pickle.dump(dict(f_c), f3)
    pickle.dump(N, fN)
