'''
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ
'''

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


from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.metrics import classification_report, precision_score, recall_score, accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_recall_curve
import numpy as np
import matplotlib.pyplot as plt

acc_cross = list()
prec_cross = list()
recl_cross = list()
f1_cross = list()

X = np.array(train_data)
y = np.array(label_list)
plot_data = []
kfold_scores = list()
skf = StratifiedKFold(n_splits=5, shuffle=True)

for k_train, k_test in skf.split(X, y):
    lr = LogisticRegression(penalty='l1', C=2.)
    lr.fit(X[k_train], y[k_train])
    # print(classification_report(y[k_test], lr.predict(X[k_test])))
    # print('Accuracy: ',accuracy_score(lr.predict(X[k_test]), y[k_test]))
    predictions = lr.predict_proba(X[k_test])[:,1]
    precision, recall, thresholds = precision_recall_curve(y[k_test], predictions)
    print("preds:", predictions)
    thresholds = np.append(thresholds, 1)
    plot_data.append({
            'thresholds': thresholds
        ,   'precision': precision
        ,   'recall': recall
    })

    for p in plot_data:
        plt.plot(p['thresholds'], p['precision'], alpha=0.3)
        plt.plot(p['thresholds'], p['recall'], alpha=0.3)

    leg = plt.legend(('Precision', 'Recall'), frameon=True)
    leg.get_frame().set_edgecolor('k')
    plt.xlabel('threshold')
    plt.ylabel('%')
    plt.title('knock79')
    plt.grid()
    plt.plot()
    plt.savefig('knock79.png')
    plt.show()
