'''
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
'''

import word2vec
from knock90 import load_model
import sys
from pprint import pprint
import json


if __name__ == '__main__':

    try:
        model = load_model()
    except:
        sys.exit(1)

    with open('countries.json') as f:
        country_json = json.load(f)

    c_vec = []
    c_label = []
    for c in country_json:
        if c['name'] in model.vocab:
            c_label.append(c['name'])
            c_vec.append(model[c['name']]) # knock 96

    #knock 99
    from matplotlib import pyplot as plt
    from sklearn.manifold import TSNE
    import numpy as np

    a = np.array(c_vec)
    # print(a.shape)
    model = TSNE(n_components=2, random_state=0, perplexity=8, learning_rate=100)
    np.set_printoptions(suppress=True)
    reduced =  model.fit_transform(a)
    # print(reduced.shape)
    print(reduced)
    plt.scatter(reduced[:, 0], reduced[:, 1])
    plt.plot()
    plt.show()
