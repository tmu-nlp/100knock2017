# ! this program is too heavy when use pred_per !
from sklearn.externals import joblib
import numpy as np
from collections import defaultdict
import pickle
from knock72 import pn_list,stem_list

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

#print(len(pn_list))
lr = joblib.load('lr.pkl')
weight = lr.coef_
bias = lr.intercept_

with open('word_ids.pkl','rb') as ids:
    word_ids = pickle.load(ids)

pl_list = []


for i,line in enumerate(stem_list):
    sent_word_id = [[0] * len(word_ids)]
    for word in stem_list[i]:
        sent_word_id[0][word_ids[word]] += 1

    pred_label = lr.predict(sent_word_id)
    pl_list.append(pred_label[0])
#    print(pred_label)
#    print(pl_list)
if __name__ == ' __main__':
    for i,line in enumerate(stem_list):
        sent_word_id = [[0] * len(word_ids)]
        for word in stem_list[i]:
            sent_word_id[0][word_ids[word]] += 1

#    print(lr.coef_[0][i])　# 推定値、偏回帰係数
#    print(lr.intercept_) # 切片
#    print(lr.predict(sent_word_id)[0]) # 予想ラベル
# 必要：正解ラベル、予想ラベル、予想確率 = ax + b形
        ans = pn_list
        pred_label = lr.predict(sent_word_id)
#    pred_per = sig(np.dot(weight.T,sent_word_id) + bias)
        print('correct:{}\tpred:{}'.format(pn_list[i],pred_label[0]))
#,pred_per[0][0]
