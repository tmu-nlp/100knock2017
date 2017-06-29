from knock72 import *
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import pickle


if __name__ == '__main__':
    logistic =  LogisticRegression()

    with open('result/ids.dump', 'rb') as data_ids_in:
        ids = pickle.load(data_ids_in)

    with open('result/sentiment.txt', 'r') as data_in:
        data_in_preprocessed, labels_correct = preprocessor_data(data_in, ids, test=1)
        features = []
        for words in data_in_preprocessed:
            features.append(create_feature(words, ids, test=1))

    with open('result/Accuracy_Precision_Recall_F_5.txt', 'w') as data_out:
        scores = ['accuracy', 'precision', 'recall', 'f1']
        metrics = [cross_val_score(logistic, features, labels_correct, cv=5, scoring=score) for score in scores]
        for score, metric in zip(scores, metrics):
            print('{}\t\t{}'.format(score, metric.mean()), file=data_out)
