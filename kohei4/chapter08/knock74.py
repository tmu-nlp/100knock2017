"""
74. 予測
73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．


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
    with open(model_file, 'r') as f:
        for ii, line in enumerate(f):
            weights = line.rstrip('\n').split('\t')
            w[weights[0]] = float(weights[1])
        #print(w.items())

    with open(input_file, 'r') as ff:
        for ii, line in enumerate(ff):
            #if ii >= 0 and ii <= 1:
                words = line.split()
                words = words[1:]
                #print(words)
                phi = create_features(words)
                prob = logistic(w,phi)
                #print(prob)
                if prob >= 0.5:
                    y_predicted =1
                    print('label prob: {} {}'.format(y_predicted, prob ))
                else:
                    y_predicted = -1
                    print('label prob: {} {}'.format(y_predicted, 1 - prob))


predict_all(model_file, input_file)
