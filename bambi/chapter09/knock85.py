from collections import defaultdict
import pickle
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import TruncatedSVD
ppmi = pickle.load(open("ppmi.pickle","rb"))
dv = DictVectorizer()
vectors = []
tokens = []
for k, v in ppmi.items():
    tokens.append(k)
    vectors.append(v)
features = dv.fit_transform(vectors)
svd = TruncatedSVD(n_components=20)
new_vectors = svd.fit_transform(features)
result = dict(zip(tokens,new_vectors))
pickle.dump(result, open("features85.pickle","wb"))
print(result["England"])
