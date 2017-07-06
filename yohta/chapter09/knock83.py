from collections import defaultdict
import pickle

f_tc = defaultdict(int)
f_t = defaultdict(int)
f_c = defaultdict(int)

if __name__ == '__main__':
    with open('data/answer82.txt') as i_f:
        pair = 0
        for line in i_f:
            tc = line.strip()
            f_tc[tc] += 1
            f_t[tc.split('\t')[0]] += 1
            f_c[tc.split('\t')[1]] += 1
            pair += 1
    with open('data/answer83','wb') as o_f:
        pickle.dump((dict(f_tc),dict(f_t),dict(f_c),pair),o_f)
