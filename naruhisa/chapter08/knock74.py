import numpy as np
import sklearn.linear_model
from sklearn.externals import joblib
from collections import defaultdict
import pickle

LRmodel = joblib.load('LRmodel.pkl')
with open('ids.pkl', 'rb') as f:
    ids_x = pickle.load(f)

with open('neo_senti.txt', 'r') as i_f:
    c_count = 0
    for count, line in enumerate(i_f):
        x = [[0 for i in range(len(ids_x))]]
        words = line.split()
        y = words[0]
        del words[0]
        for word in words:
            x[0][ids_x[word]] += 1
        if y == LRmodel.predict(x)[0]:
            c_count += 1
    print('正答率', c_count / (count + 1))
