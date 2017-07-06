import pickle
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import TruncatedSVD

if __name__ == '__main__':
    with open('84_X','rb') as data:
        X = pickle.load(data)
    tokens = []
    vectors = []
    for word_set, value in X.items():
        tokens.append(word_set)
        vectors.append(value)
    vec = DictVectorizer()
    features = vec.fit_transform(vectors)
    svd = TruncatedSVD(n_components = 300)
    vector = svd.fit_transform(features)
    feature_set = dict(zip(tokens,vector))
    with open('85_feature','wb') as data:
        pickle.dump(feature_set,data)

