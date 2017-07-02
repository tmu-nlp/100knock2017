import numpy as np
import sklearn.linear_model
from collections import defaultdict
import pickle

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

with open('ids.pkl', 'rb') as f:
    ids_x = pickle.load(f)
with open('neo_senti.txt', 'r') as f:
    for text_count, line in enumerate(f):
        pass

with open('neo_senti.txt', 'r') as i_f:
    LR_model = sklearn.linear_model.LogisticRegression()
    X = list()
    Y = list()
    test_flag = False
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for count, line in enumerate(i_f):
        x = [0 for i in range(len(ids_x))]
        words = line.split()
        y = words[0]
        del words[0]
        for word in words:
            x[ids_x[word]] += 1
        if test_flag:
            p_y = LR_model.predict([x])

            if p_y[0] == '+1' and y == '+1':
                tp += 1
            elif p_y[0] == '+1' and y == '-1':
                fp += 1
            elif p_y[0] == '-1' and y == '-1':
                tn += 1
            elif p_y[0] == '-1' and y == '+1':
                fn += 1
        else:
            X.append(x)
            Y.append(y)

        if count == int(text_count / 5):
            LR_model.fit(X, Y)
            test_flag = True


    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (fp + tp)
    recall = tp / (tp + fn)
    F_measure = 2 * precision * recall / (precision + recall)
    print('正解率：{}\n適合率：{}\n再現率：{}\nF1スコア：{}' .format(accuracy, precision, recall, F_measure))
