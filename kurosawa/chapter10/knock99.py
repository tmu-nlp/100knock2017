import pickle
from collections import defaultdict
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

if __name__ == '__main__':
    country_model = pickle.load(open('country_model.pickle','rb'))
    tokens = []
    vectors = []
    for word_set, value in country_model.items():
        tokens.append(word_set)
        vectors.append(value)
    model = TSNE(n_components=2, perplexity=50, n_iter=500, verbose=3, random_state=1)
    X = model.fit_transform(vectors)
    plt.clf()
    plt.scatter(X[:,0],X[:,1],c='w')
    for k,v,s in zip(tokens,X[:,0],X[:,1]):
        plt.annotate(k,xy=(v,s))
    plt.show()
