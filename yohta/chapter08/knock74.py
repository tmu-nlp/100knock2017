from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from knock72 import *
import pickle

lr = joblib.load('lr.pkl')
with open('word_ids.pkl','rb') as id_f:
    word_ids = pickle.load(id_f)

with open('sentiment.txt','r') as i_f:
    correct = 0
    count = 0
    for line in i_f:
        count += 1
        feature = [[0] * len(word_ids)]
        pn,sentence = int(line[:2].strip('+')),pre(line[3:])
        words = sentence.split()
        for word in words:
            if return_TF(word):
                continue
            if len(word) <= 1:
                continue
            stemmed_word = stemming(word)
            feature[0][word_ids[stemmed_word]] += 1
#        print(pn)
        if pn == lr.predict(feature)[0]:
            correct += 1
    print('正答率 : {} %'.format(correct*100/count))
