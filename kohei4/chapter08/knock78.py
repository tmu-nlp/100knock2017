"""
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
"""

import sys
import math
from collections import defaultdict
from stemming.porter2 import stem




n_iter = 3
eta = 1
#train_input = "../../data/03-train-input.txt"
model_file = "per_model.txt"
input_file = "sentiment.txt"

data = []

def create_features(x, feature_set):
    phi = defaultdict(lambda: 0)

#    words = x.split()
    for word in x:
        if stem(word) in feature_set:
            phi["UNI:" + word] += 1

    return phi


def test_create_features(x):
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

def update_w(w,phi,y):
    for name in phi.keys():

        if y == 1:
            w[name] += eta*phi[name]*math.exp(w[name]*phi[name])\
            /math.pow((1+math.exp(w[name]*phi[name])),2)


        else:
            w[name] += -eta*phi[name]*math.exp(w[name]*phi[name])\
            /math.pow((1+math.exp(w[name]*phi[name])),2)
            #print('y=-1,name,w',name,w[name])




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

def predict_all(w_dict, test_d):
    data = []
    for ii, line in enumerate(test_d):
        #if ii >= 0 and ii <= 10:
        words = line.split()
        label = int(words[0])
        words = words[1:]
        #print(label,words)

        phi = test_create_features( words )
        prob = logistic(w,phi)
        #print(prob)
        if prob >= 0.5:
            y_predicted =1
            data.append([label,y_predicted, prob])
        else:
            y_predicted = -1
            data.append([label,y_predicted, 1 - prob])

    return data

def check_f(predicted):
# 結果を読み込んで集計
    TrPo = 0      #   予想が+1、正解も+1
    FaPo = 0      #   予想が+1、正解は-1
    FaNe = 0      #   予想が-1、正解は+1
    TrNe = 0      #   予想が-1、正解も-1


    for flag in predicted:
        #print(flag)
        if flag[0] == 1:         # label
            if flag[1] == 1:     # predicted
                TrPo += 1
            elif flag[1] == -1:
                FaNe += 1
        elif flag[0] == -1:
            if flag[1] == 1:
                FaPo += 1
            elif flag[1] == -1:
                TrNe += 1

    accuracy = (TrPo + TrNe) / (TrPo + FaPo + FaNe + TrNe)
    precision = TrPo / (TrPo + FaPo)
    recall = TrPo / (TrPo + FaNe)
    f_m = (2 * recall * precision) / (recall + precision)

    return accuracy, precision, recall, f_m



if __name__ == "__main__":

    with open('featureset.txt','r') as gg:
        feature_set = {x.strip() for x in gg}
        #print(feature_set)

    with open(input_file, 'r') as ff:
        all_input = list(ff)
        # len(all_input) = 10662
        #print(len(all_input))
        #print(all_input)
        unit = len(all_input)//5
        #print(len(all_input)-5*unit)

    #for ii in range(5):
    unit_l = []
    for ii in range(5):
        accuracy_s = 0
        precision_s = 0
        recall_s = 0
        f_m_s = 0
        unit_l.append(all_input[ unit*ii : unit*(ii+1) ])

    with open('78result', 'w' ) as hh:
        for jj in range(5):
        #for jj in range(1):
            w = dict()

            print(jj+1,'/5',file=hh)
            data = []
            test_d = []
            learn_d = []
            for kk in range(5):
                if jj == kk:
                    test_d = unit_l[kk]
                else:
                    learn_d += unit_l[kk]

            #print(len(test_d))
            #print(len(learn_d))
            for line in learn_d:
                words = line.strip().split()
                data.append([float(words[0]),words[1:]])

            #print(data)

            for _ in range(n_iter):
                for y, x in data:
                    phi = create_features(x,feature_set)
                    #print(phi.items())
                    #print(y)
                    y_prob = logistic(w,phi)
                    #print(y_prob)
                    update_w(w,phi,y)

            with open('permodel_five.txt','w') as ff:
                for key,value in w.items():
                    #print(key,value)
                    print("{}\t{}".format(key, value),file = ff)

            #判別開始

            predicted = predict_all(w, test_d)
            #print(predicted)

            accuracy, precision, recall, f_m = check_f(predicted)
            print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
                accuracy, precision, recall, f_m),file=hh)
            accuracy_s += accuracy
            precision_s += precision
            recall_s += recall
            f_m_s += f_m


            if jj == 4:
                print('\nResult(averaged)', file= hh)
                print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
                    accuracy_s/5, precision_s/5, recall_s/5, f_m_s/5),file=hh)
