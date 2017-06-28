import nltk
from knock71 import is_stopword
from collections import defaultdict
from pprint import pprint

stemmer = nltk.PorterStemmer()
# lemmatizer = nltk.WordNetLemmatizer()

ids = defaultdict(lambda:len(ids))

def create_features(_words:list) -> list:
    _phi = [0] * len(ids)
    for word in _words:
        if not is_stopword(word):
            stemed = stemmer.stem(word)
            _phi[ids[word]] += 1
    return _phi

def create_ids(_words):
    for word in _words:
        ids[word]


train_data = list()
label_list = list()

label = 0
words = list()

with open('sentiment.txt') as f:
    for line in f:
        label, words = int(line.split()[0]), line.split()[1:]
        create_ids(words)
        
with open('sentiment.txt') as f:
    for line in f:
        label, words = int(line.split()[0]), line.split()[1:]
        label_list.append(label)
        feat = create_features(words)
        train_data.append(feat)

'''
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
'''

from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold
import numpy as np

acc_cross = list()
prec_cross = list()
recl_cross = list()
f1_cross = list()

X = np.array(train_data)
y = np.array(label_list)

kfold_scores = list()
skf = StratifiedKFold(n_splits=5, shuffle=True)
for k_train, k_test in skf.split(X, y):
    lr = LogisticRegression(penalty='l1', C=2.)
    lr.fit(X[k_train], y[k_train])
    print(classification_report(y[k_test], lr.predict(X[k_test])))
    print('Accuracy: ',accuracy_score(lr.predict(X[k_test]), y[k_test]))
    
#     scores_dict = dict()
#     acc = accuracy_score(lr.predict(X[k_test]), y[k_test])    
#     prec = precision_score(lr.predict(X[k_test]), y[k_test])    
#     recl = recall_score(lr.predict(X[k_test]), y[k_test])    
#     f1 = f1_score(lr.predict(X[k_test]), y[k_test])    
#     scores_dict['acc'] = acc
#     scores_dict['prec'] = prec
#     scores_dict['recl'] = recl
#     scores_dict['f1'] = f1
#     kfold_scores.append(scores_dict)
#
# print(' --------- knock78 ----------\n\n')

# for idx, scr in enumerate(kfold_scores):
#     for k,v in scr.items():
#         print('{}: {} -> {}'.format(idx, k, v))

