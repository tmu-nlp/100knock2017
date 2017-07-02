"""
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，
適合率-再現率グラフを描画せよ．
"""

import sys
import math
from collections import defaultdict
from stemming.porter2 import stem
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
mpl.rcParams['font.family'] = 'Arial Unicode MS'

n_iter = 10
eta = 1

#train_input = "../../data/03-train-input.txt"
model_file = "per_model.txt"
input_file = "sentiment.txt"
storefile = "79_temp.txt"
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

def predict_all(model_file, input_file, thresh = 0.5):
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
                if prob >= thresh:
                    y_predicted =1
                    data.append([label,y_predicted, prob])
                else:
                    y_predicted = -1
                    data.append([label,y_predicted, 1 - prob])

    return data

def check_f(result_file):
# 結果を読み込んで集計
    TrPo = 0      #   予想が+1、正解も+1
    FaPo = 0      #   予想が+1、正解は-1
    FaNe = 0      #   予想が-1、正解は+1
    TrNe = 0      #   予想が-1、正解も-1


    with open(result_file) as gg:
        for line in gg:
            flag = line.split('\t')
            #print(cols)

            if flag[0].strip() == '1':         # label
                if flag[1].strip() == '1':     # predicted
                    TrPo += 1
                elif flag[1].strip() == '-1':
                    FaNe += 1
            elif flag[0].strip() == '-1':
                if flag[1].strip() == '1':
                    FaPo += 1
                elif flag[1].strip() == '-1':
                    TrNe += 1


    accuracy = (TrPo + TrNe) / (TrPo + FaPo + FaNe + TrNe)
    precision = TrPo / (TrPo + FaPo)
    recall = TrPo / (TrPo + FaNe)
    f_m = (2 * recall * precision) / (recall + precision)

    return accuracy, precision, recall, f_m


th_l = []
prc_l = []
rec_l = []

for ii, thresh in enumerate(np.arange(0.05, 1.0, 0.05)):

        data = predict_all(model_file, input_file, thresh)

        with open(storefile, 'w') as gg:
            for i, j, k in data:
                print(i,'\t',j,'\t',k, file= gg)

        accuracy, prc, rec, f_m = check_f(storefile)
        #print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
        #    accuracy, precision, recall, f_m))
        th_l.append(thresh)
        prc_l.append(prc)
        rec_l.append(rec)

#print(th_l,prc_l,rec_l)

#pyplot.plot(th_l,prc_l)
#pyplot.plot(th_l,rec_l)

#pyplot.show()

plt.plot(prc_l, rec_l, label = '再現率')
plt.plot(prc_l, th_l, label = '閾値')
plt.title('適合率 VS 再現率、閾値')
plt.legend()

plt.show()
