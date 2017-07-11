'''
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．

'''


import word2vec
from knock90 import load_model
import sys
from pprint import pprint

if __name__ == '__main__':

    try:
        model = load_model()
    except:
        sys.exit(1)

    vecs = list()
    with open('out91') as f:
        for line in f:
            _vec = line.strip().split()
            vecs.append(_vec)
            # print(_vec)

    rare_words = list()

    for v in vecs:
        try:
            indexes, metrics = model.analogy(pos=[v[1], v[2]], neg=[v[0]], n=1)
            word = model.generate_response(indexes, metrics).tolist()[0][0]
            prob = model.generate_response(indexes, metrics).tolist()[0][1]
            print('{} {} {}'.format(' '.join(v), word, prob))
        except KeyError:
            word = 'none'
            prob = 'none'
            print('{} {} {}'.format(' '.join(v), word, prob))
            rare_words.append(v)
    # print('--------rare words--------\n')
    # pprint(rare_words)
