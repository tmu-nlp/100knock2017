from knock72 import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
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

    with open('result/Accuracy_Precision_Recall_F.txt', 'w') as data_out:
        label_predict = logistic.predict(features)
        print('Accuracy : {}\n'.format(accuracy_score(labels_correct, label_predict)), file=data_out)
        print(classification_report(labels_correct, label_predict), file=data_out)
