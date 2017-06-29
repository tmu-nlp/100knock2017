"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，
重みの低い素性トップ10を確認せよ

"""

import sys
import math
from collections import defaultdict
from stemming.porter2 import stem

n_iter = 10
eta = 1
#train_input = "../../data/03-train-input.txt"
model_file = "per_model.txt"
output_file = "ranking.txt"
w = dict()
data = []

with open(model_file, 'r') as ff:
    for lines in ff:
        word, prob = lines.strip().split('\t')
        word = word[4:]
        prob = float(prob)
        abs_prb = abs(prob)
        data.append([word,prob,abs_prb])

#print(data)

data = sorted(data, key=lambda x: x[2])
data_max = data[-1:-11:-1]
data_min = data[0:10]

print('重みの高い順')
for ii in range(10):
    print('{}\t{}'.format(data_max[ii][0],data_max[ii][1]))

print()

print('重みの低い順')
for ii in range(10):
    print('{}\t{}'.format(data_min[ii][0],data_min[ii][1]))
