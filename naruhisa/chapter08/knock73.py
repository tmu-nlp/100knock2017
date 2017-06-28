import numpy as np
import sklearn.linear_model
from sklearn.externals import joblib
from collections import defaultdict
import pickle

ids_x = defaultdict(lambda: len(ids_x))
with open('neo_senti.txt', 'r') as f:
    for line in f:
        words = line.split()
        del words[0]
        for word in words:
            ids_x[word]
with open('neo_senti.txt', 'r') as f:
    Y = list()
    X = list()
    for line in f:
        x = [0] * len(ids_x)
        words = line.split()
        Y.append(words[0])
        del words[0]
        for word in words:
            x[ids_x[word]] += 1
        X.append(x)

estimator = sklearn.linear_model.LogisticRegression()
estimator.fit(X, Y)

with open('ids.pkl', 'wb') as f:
    pickle.dump(dict(ids_x), f)
joblib.dump(estimator, 'LRmodel.pkl')
