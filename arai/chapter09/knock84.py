import pickle
import math
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer

ppmi_dic = defaultdict(dict)
t_c_dic, t_dic, c_dic, N = pickle.load(open('knock83.txt', 'rb'))

ppmi = lambda key: max(math.log(N * t_c_dic[key] / (t_dic[key.split(' ')[0]] * c_dic[key.split(' ')[1]])), 0)

for t_c, freq in t_c_dic.items():
    if freq >= 10:
        t, c =t_c.split()
        ppmi_tc = ppmi(t_c)
        if ppmi_tc > 0:
            ppmi_dic[t][c] = ppmi_tc

dicvec = DictVectorizer()
matrix = dicvec.fit_transform(ppmi_dic.values())

with open('knock84.txt','wb') as w_f:
    pickle.dump((matrix, list(ppmi_dic.keys())), w_f)
        
        

