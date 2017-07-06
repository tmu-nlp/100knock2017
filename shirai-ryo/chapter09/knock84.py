from collections import defaultdict
import pickle
import math

f_tc = pickle.load(open('f_tc_83', 'rb'))
f_t = pickle.load(open('f_t_83', 'rb'))
f_c = pickle.load(open('f_c_83', 'rb'))
N = pickle.load(open('N_83', 'rb'))

X = defaultdict(dict)

for tc, count in f_tc.items():
    t, c = tc.split()
    if count >= 50:
        PPMI = max(math.log2((N*count) / (f_t[t]*f_c[c])), 0)
        #print(PPMI)
        if PPMI != 0:
            X[t][c] = PPMI

with open('X_84', 'wb') as Xtc:
    pickle.dump(X, Xtc)

# python -m pickle 'ファイル名' でピックルの中身を確認でき
# る
