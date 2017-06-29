from knock73 import feature, feature_vector
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
import numpy as np
import sys


def fit_feature(query, feature_dict):
    dicvec = DictVectorizer()
    dicvec.fit_transform([feature_dict])
    return (dicvec.transform([dict(feature_vector(query))]))

def predict(LR, feature):
    polarity = '+1' if LR.predict(feature)[0] == 1 else '-1'
    probability = LR.predict_proba(feature)[0]
    return polarity, probability

def load_dict(f_name):
    feature_dict = dict()
    for line in open(f_name):
        word, value = line.strip().split()
        feature_dict[word] = int(value)
    return feature_dict

if __name__ == '__main__':
    feature_dict = load_dict('knock72_file.txt')
    LR = joblib.load('LR.pkl')
    for line in open('sentiment.txt'):
        label, sentence = line.split('\t')
        query = sentence.split()
        feature = fit_feature(query, feature_dict)
        polarity, probability = predict(LR, feature)
        
        print(label, polarity, max(probability[0], probability[1]))

    
