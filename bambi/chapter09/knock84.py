from collections import defaultdict
import pickle
import math
N = pickle.load(open('N.pickle', 'rb'))
f_c = pickle.load(open('f_c.pickle', 'rb'))
f_t = pickle.load(open('f_t.pickle', 'rb'))
f_tc = pickle.load(open('f_tc.pickle', 'rb'))
bar = 50
x = defaultdict(dict)
for tc, f in f_tc.items():
    t,c = tc.split("\t")
    if f >= bar:
        pmi = math.log((N * f )/(f_t[t]*f_c[c] ),2)
        ppmi = max(pmi,0) # if not bigger than 0, choose 0
        x[t][c] = ppmi
        #print("{}\t\t{}".format(tc,ppmi))
pickle.dump(dict(x),open("ppmi.pickle","wb"))
print("finished")
