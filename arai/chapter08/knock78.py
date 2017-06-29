from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from knock73 import feature, feature_vector, train, create_feature
from knock74 import fit_feature, load_dict
from knock76 import predict
import scipy

def cv(feature_dict, feature, polarity, folds):
    kfold = KFold(len(polarity), n_folds = folds)
    count, f1, recall, precision, accuracy = 0, 0, 0, 0, 0
    for train, test in kfold:
        LR = LogisticRegression()
        count += 1
        x = [(feature[i]) for i in train]
        y = [(polarity[i])for i in train]
        LR.fit(scipy.sparse.vstack(x), (y))

        test_label = []
        answer_label = [(polarity[j]) for j in test]
        for j in test:
            query = feature[j]
            result = -1 if query.shape[1] != len(feature_dict) else predict(LR, query)
            test_label.append(int(result[0]))
        accuracy += accuracy_score(answer_label, test_label)
        precision += precision_score(answer_label, test_label)
        recall += recall_score(answer_label, test_label)
        f1 += f1_score(answer_label, test_label)
        print('{}_fold finished.'.format(count))
    return accuracy, precision, recall, f1

if __name__ == '__main__':
    feature_dict = load_dict('knock72_file.txt')
    feature, polarity = create_feature(open('sentiment.txt'))
    threshold = 0.5
    folds = 5
    accuracy, precision, recall, f1 = cv(feature_dict, feature, polarity, folds)
    print('accuracy: {}'.format(accuracy / 5))
    print('precision: {}'.format(precision / 5))
    print('recall: {}'.format(recall / 5))
    print('F1: {}'.format(f1 / 5))





