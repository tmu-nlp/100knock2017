from knock72 import *
from sklearn.linear_model import LogisticRegression
import pickle


if __name__ == '__main__':
    with open('result/ids.dump', 'rb') as data_ids_in:
        ids = pickle.load(data_ids_in)

    with open('result/logistic.dump', 'rb') as data_logistic_in:
        logistic = pickle.load(data_logistic_in)

    with open('result/sentiment.txt', 'r') as data_in:
        data_in_preprocessed, labels_correct = preprocessor_data(data_in, ids, test=1)
        features = []
        for words in data_in_preprocessed:
            features.append(create_feature(words, ids, test=1))

    with open('result/correct_predict_prob.txt', 'w') as data_out:
        for i, j, k in zip(labels_correct, logistic.predict(features), logistic.predict_proba(features)):
            print('correct : {}\t\tpredict : {}\t\tprobability : {}'.format(i, j, max(k)), file=data_out)
