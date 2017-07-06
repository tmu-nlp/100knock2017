import pickle
from collections import defaultdict
def read(f):
    for l in f:
        yield l
if __name__ == "__main__":
    f_tc = defaultdict(int)
    f_t = defaultdict(int)
    f_c = defaultdict(int)
    N = 0
    tokens = pickle.load(open("tokens82.pickle","rb"))
    for token in read(tokens):
        tc = token.strip('\n')
        t,c = tc.split("\t")
        f_tc[tc] += 1
        f_t[t] += 1
        f_c[c] += 1
        N += 1
    pickle.dump(dict(f_tc), open("f_tc.pickle", "wb" ) )
    pickle.dump(dict(f_t), open("f_t.pickle", "wb" ) )
    pickle.dump(dict(f_c), open("f_c.pickle", "wb" ) )
    pickle.dump(N, open("N.pickle", "wb" ) )
    print("finished")
