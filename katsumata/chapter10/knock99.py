import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pickle
import numpy as np

if __name__ == '__main__':
    country_name = list()
    with open('country_vec.dump', 'rb') as feat_f:
        country_dict = pickle.load(feat_f)
    for id_num, item in enumerate(country_dict.items()):
        country_name.append(item[0])
        if id_num == 0:
            country_mat = item[1]
            continue
        country_mat = np.vstack((country_mat, item[1]))
    X_reduced = TSNE(n_components=2).fit_transform(country_mat)
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c='snow')
    for s,x,y in zip(country_name,X_reduced[:,0], X_reduced[:,1]):
        plt.annotate(s, xy=(x,y))
    plt.show()
