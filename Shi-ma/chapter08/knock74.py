from knock72 import *
from sklearn.linear_model import LogisticRegression
import pickle


if __name__ == '__main__':
    with open('result/ids.dump', 'rb') as data_ids_in:
        ids = pickle.load(data_ids_in)

    with open('result/logistic.dump', 'rb') as data_logistic_in:
        logistic = pickle.load(data_logistic_in)

    with open('result/sumple.txt', 'r') as data_in:
        features = []
        for line in data_in:
            words = line.split()
            words_preprocessed = preprocessor_words(words)
            features.append(create_feature(words_preprocessed, ids, test=1))

    with open('result/predict_label_prob.txt', 'w') as data_out:
        for i, j in zip(logistic.predict(features), logistic.predict_proba(features)):
            print('predict : {}\n{}'.format(i, max(j), file=data_out))
