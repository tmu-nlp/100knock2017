import pickle
from collections import defaultdict
from sklearn.cluster import KMeans
import numpy as np
from sklearn.feature_extraction import DictVectorizer

if __name__ == '__main__':
    country_model = pickle.load(open('country_model.pickle','rb'))
    tokens = []
    vectors = []
    for word_set, value in country_model.items():
        tokens.append(word_set)
        vectors.append(value)
    pred = KMeans(n_clusters=5).fit_predict(vectors)
    cluster = defaultdict(list)
    for i in range(len(pred)):
        cluster[pred[i]].append(tokens[i])
    for j in range(5):
        print('cluster{}:{}\n'.format(j,cluster[j]))
