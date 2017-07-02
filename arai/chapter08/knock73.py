#from knock72 import feature
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from collections import defaultdict
from sklearn.externals import joblib
from nltk.stem import PorterStemmer
from knock71 import stopwords

def feature(sentence):
    features = []
    stemmer = PorterStemmer()
    for word in sentence:
        stem_word = stemmer.stem(word)
        if stopwords(stem_word) == False:
            features.append(stem_word)
    return features
        
def feature_vector(sentence):
    wordvector = defaultdict(int)
    for word in sentence :
        wordvector[word] += 1
    return wordvector

def create_feature(sent_list):
    feature_ = []
    polarity = []
# ↑極性リスト
    features_ = []
# ↑素性リスト
#　↓二値化
    vec = DictVectorizer()

    for line in sent_list:
        sentence = line.strip('\n').split()
        sentence2 = sentence.pop(0)
        polarity.append(int(sentence2))
        #print(polarity)
        feature_ = feature(sentence)
        '''
        for word in feature(sentence):
            feature_.append(word)
            print(feature_)
            '''
        features_.append(feature_vector(feature_))
    x_feature = vec.fit_transform(features_)
    return x_feature, polarity


def train(x_feature, polarity):
    LR = LogisticRegression()
    LR.fit(x_feature, polarity)
    return LR

if __name__ == '__main__':
    with open('sentiment.txt') as text:
        x_feature, polarity = create_feature(text)
        LR = train(x_feature, polarity)
        joblib.dump(LR, 'LR.pkl')

