from knock72 import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
import pickle
import matplotlib.pyplot as plt


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

    result = logistic.predict_proba(features)

    thres = [i/100 for i in range(2, 100, 2)]
    precision = []
    recall = []
    for thre in thres:
        labels_predict = list(map(lambda x: 1 if x[1] >= thre else -1, result))
        precision.append(precision_score(labels_correct, labels_predict))
        recall.append(recall_score(labels_correct, labels_predict))

    plt.plot(thres, precision, label='precision')
    plt.plot(thres, recall, label='recall')
    plt.legend()
    plt.savefig('result/threshold_precision_recall.png')
