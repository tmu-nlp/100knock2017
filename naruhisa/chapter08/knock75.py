import numpy as np
import sklearn.linear_model
from sklearn.externals import joblib
from collections import defaultdict
import pickle

LRmodel = joblib.load('LRmodel.pkl')
with open('ids.pkl', 'rb') as f:
    ids_x = pickle.load(f)
x_ids = dict()
x_w = dict()
for k, v in ids_x.items():
    x_ids[v] = k

for id_x, w in enumerate(LRmodel.coef_[0]):
    x_w[x_ids[id_x]] = w

rank = 0
for word, w in sorted(x_w.items(), key = lambda x:x[1], reverse = True):
    rank += 1
    print('{}:{} {}' .format(rank, word, w))
    if rank > 9:
        break
rank = 0
for word, w in (sorted(x_w.items(), key = lambda x:x[1], reverse = False)):
    rank += 1
    print('{}:{} {}' .format(rank, word, w))
    if rank > 9:
        break
