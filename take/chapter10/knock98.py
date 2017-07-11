'''
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
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

    from matplotlib import pyplot as plt
    from scipy.cluster.hierarchy import dendrogram, linkage
    import numpy as np

    lk = linkage(c_vec, method='ward')
    dendrogram(lk, p=20, truncate_mode='lastp', labels=c_label)
    plt.show()
