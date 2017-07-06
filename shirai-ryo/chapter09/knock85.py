from collections import defaultdict
import pickle
import numpy as np
from sklearn.feature_extraction import DictVectorizer
# 語のリストから単語文書行列を作る
from sklearn.decomposition import TruncatedSVD
# 特徴量の次元圧縮
# n_componentsが圧縮後の次元数(下では50にしてある)

ppmi = pickle.load(open("X_84","rb"))
dv = DictVectorizer()

vectors = []
tokens = []
for k, v in ppmi.items():
    tokens.append(k)
    vectors.append(v)
features = dv.fit_transform(vectors)
svd = TruncatedSVD(n_components=50)
new_vectors = svd.fit_transform(features)
result = dict(zip(tokens,new_vectors))

pickle.dump(result, open("85.pickle","wb"))


# from sklearn.feature_extraction import DictVectorizer
# v = DictVectorizer()
# v.fit_transform([{'a': 3, 'b': 1, 'd': 1}, {'a': 1, 'c': 3, 'd': 2}]).toarray()
# # => array([[ 3.,  1.,  0.,  1.],
# #           [ 1.,  0.,  3.,  2.]])
