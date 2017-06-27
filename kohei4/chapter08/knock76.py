"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，
予測確率をタブ区切り形式で出力せよ．
"""

import sys
import math
from collections import defaultdict
from stemming.porter2 import stem

n_iter = 10
eta = 1
#train_input = "../../data/03-train-input.txt"
model_file = "per_model.txt"
input_file = "sentiment.txt"
w = dict()
data = []

def create_features(x):
    phi = defaultdict(lambda: 0)

#    words = x.split()
    for word in x:
        word = stem(word)
        phi["UNI:" + word] += 1

    return phi

def sigmoid(x):
  return 1.0 / (1.0 + math.exp(-x))

def logistic(w,phi):
    score = 0
    for name in phi.keys():
        if (name in w) == False:
            w[name] = 0
        score += phi[name]*w[name]
        #print('score', score)

    prob = sigmoid(score)
    return prob

def predict_one(w,phi):
    score=0
    for name in phi.keys():
        if (name in w) == False:
            w[name] = 0

        score += phi[name]*w[name]

        #print(w.items())

    if score >= 0:
        return 1
    else:
        return -1

def predict_all(model_file, input_file):
    data = []
    with open(model_file, 'r') as f:
        for ii, line in enumerate(f):
            weights = line.rstrip('\n').split('\t')
            w[weights[0]] = float(weights[1])
        #print(w.items())

    with open(input_file, 'r') as ff:
        for ii, line in enumerate(ff):
            #if ii >= 0 and ii <= 10:
                words = line.split()
                label = int(words[0])
                words = words[1:]
                phi = create_features(words)
                prob = logistic(w,phi)
                #print(prob)
                if prob >= 0.5:
                    y_predicted =1
                    data.append([label,y_predicted, prob])
                else:
                    y_predicted = -1
                    data.append([label,y_predicted, 1 - prob])

    return data

data = predict_all(model_file, input_file)

for i, j, k in data:
    print(i,'\t',j,'\t',k)
