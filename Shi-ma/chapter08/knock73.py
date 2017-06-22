from knock72 import *
from sklearn.linear_model import LogisticRegression
import pickle

if __name__ == '__main__':
    features = []
    with open('result/ids.dump', 'rb') as data_ids_in:
        ids = pickle.load(data_ids_in)

    with open('result/sentiment.txt', 'r') as data_in:
        data_in_preprocessed, labels = preprocessor_data(data_in, ids)
    for words in data_in_preprocessed:
        features.append(create_feature(words, ids))

    logistic =  LogisticRegression()
    logistic_model = logistic.fit(features, labels)

    with open('result/logistic.dump', 'wb') as data_logistic_out:
        pickle.dump(logistic_model, data_logistic_out)
