import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

if __name__ == '__main__':
    co_list = list()
    with open('data/knock96.dump','rb') as i_f:
        model_dict = pickle.load(i_f)
    for num,item in enumerate(model_dict.items()):
        co_list.append(item[0])
        if num == 0:
            mat = item[1]
            continue
        mat = np.vstack((mat, item[1]))
    X_reduced = TSNE(n_components=2).fit_transform(mat)
    plt.scatter(X_reduced[:,0], X_reduced[:,1], c='white')
    for s,x,y in zip(co_list,X_reduced[:,0], X_reduced[:,1]):
        plt.annotate(s,xy=(x,y))
    plt.show()
