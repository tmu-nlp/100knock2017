'''
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．

97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5k=5として実行せよ．

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
        pprint(c['name'])
        if c['name'] in model.vocab:
            c_label.append(c['name'])
            c_vec.append(model[c['name']]) # knock 96
            # print(model[c['name']][:5])

    # knock96
    for x,y in zip(c_vec, c_label):
        print('{}\t{}'.format(x,y))

    # knock 97
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=5, random_state=1).fit(c_vec)
    pred_labels = kmeans.labels_
    
    result = {y:lab for y, lab in zip(c_label, pred_labels)}
    # for y, lab in zip(c_label, pred_labels):
    #     print('{}\t{}'.format(y, lab))
    pprint(sorted(result.items(), key=lambda x:x[1]))
