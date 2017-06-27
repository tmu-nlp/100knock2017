import numpy as np
import sklearn.linear_model
from sklearn.externals import joblib
from collections import defaultdict
import pickle

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

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

        w = LRmodel.coef_
        b = LRmodel.intercept_
        p_y = LRmodel.predict(x)
        p_y_x = sigmoid(np.dot(x, w.T) + b)
        if p_y[0] == '+1':
            p_y_x = 1 - p_y_x
        print('{}   {}  {}' .format(y, p_y[0], p_y_x[0][0]))
