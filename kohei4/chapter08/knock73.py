"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

   -----------
Parameters
    ------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.
NLPtutorial5 で使ったデータでの成績
../../../NLPtutorial2017/script/grade-prediction.py
../../../NLPtutorial2017/data/titles-en-test.labeled myanswer.txt
Accuracy = 87.530995%
"""

import sys
import math
from collections import defaultdict
from stemming.porter2 import stem

n_iter = 50
eta = 1

#train_input = "../../data/03-train-input.txt"
input_file = "sentiment.txt"
w = dict()
data = []

def create_features(x, feature_set):
    phi = defaultdict(lambda: 0)

#    words = x.split()
    for word in x:
        if stem(word) in feature_set:
            phi["UNI:" + word] += 1

    return phi

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
    #return prob


def update_w(w,phi,y):
    for name in phi.keys():

        if y == 1:
            w[name] += eta*phi[name]*math.exp(w[name]*phi[name])\
            /math.pow((1+math.exp(w[name]*phi[name])),2)


        else:
            w[name] += -eta*phi[name]*math.exp(w[name]*phi[name])\
            /math.pow((1+math.exp(w[name]*phi[name])),2)
            #print('y=-1,name,w',name,w[name])


with open(input_file,'r') as ff:
    for ii, line in enumerate(ff):
        #if ii >= 0 and ii <= 1:
            words = line.split()
            data.append([float(words[0]),words[1:]])
            #print(words[1:])
with open('featureset.txt','r') as gg:
    feature_set = {x.strip() for x in gg}
    #print(feature_set)


for _ in range(n_iter):
    for y, x in data:
        phi = create_features(x,feature_set)
        #print(phi.items())
        #print(y)
        y_prob = logistic(w,phi)
        #print(y_prob)
        update_w(w,phi,y)

for key,value in w.items():
    #print(key,value)
    print("{}\t{}".format(key, value))
