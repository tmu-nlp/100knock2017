import pickle
from sklearn.decomposition import TruncatedSVD

ppmi, keys = pickle.load(open('knock84.txt', 'rb'))

svd = TruncatedSVD(n_components = 50)
new_vectors = svd.fit_transform(ppmi)

word2vec = dict(zip(keys, new_vectors))
pickle.dump(word2vec, open('knock85.txt', 'wb'))




