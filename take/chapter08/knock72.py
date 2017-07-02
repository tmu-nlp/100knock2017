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


''' knock 73 '''
import dill
with open("ids.dill", 'wb') as f:
    dill.dump(ids, f)


from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

try:
    lr = joblib.load('lr.pkl')
    print("load success")
except:
    print("load fail. start training")
    lr = LogisticRegression()
    lr.fit(train_data, label_list)
    joblib.dump(lr, 'lr.pkl')


 ''' knock74 '''
score = lr.score(train_data, label_list)
print('score:{}'.format(score))


'''
knock76
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
'''

pred = lr.predict(train_data)
score = lr.predict_proba(train_data)

with open('knock76.out', 'w') as f:
    f.write('label\tpredict\tprob\n')
    for i,d in enumerate(train_data):
        print('{}\t{}\t{}'.format(label_list[i], pred[i], max(score[i])), file=f)

