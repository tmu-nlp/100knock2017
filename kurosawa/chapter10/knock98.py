import pickle
from collections import defaultdict
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage,dendrogram
from matplotlib.pyplot import show


if __name__ == '__main__':
    country_model = pickle.load(open('country_model.pickle','rb'))
    tokens = []
    vectors = []
    for word_set, value in country_model.items():
        tokens.append(word_set)
        vectors.append(value)
    pred = linkage(vectors)
    print(pred)
    dendrogram(pred,labels=tokens)
    show()
