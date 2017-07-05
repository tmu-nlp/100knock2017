from collections import defaultdict
import pickle

t_c_dic = defaultdict(int)
t_dic = defaultdict(int)
c_dic = defaultdict(int)

for line in open('knock82.txt'):
    t, c  = line.split('\t')
    cs = c.split()
    t_dic[t] += 1 
    for c in cs:
        t_c_dic[t + ' ' + c] += 1
        c_dic[c] += 1
N = sum(t_c_dic.values())

with open('knock83.txt', 'wb') as w_f:
    pickle.dump((dict(t_c_dic), dict(t_dic), dict(c_dic), N), w_f)



