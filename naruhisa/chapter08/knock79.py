import numpy as np
import sklearn.linear_model
from collections import defaultdict
import pickle
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt


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
    p_y = list()
    t_y = list()
    for count, line in enumerate(i_f):
        x = [0 for i in range(len(ids_x))]
        words = line.split()
        y = words[0]
        del words[0]
        if y == '-1':
            y = 0
        elif y == '+1':
            y = 1
        for word in words:
            x[ids_x[word]] += 1
        if test_flag:
            p_y.append(LR_model.predict_proba([x])[0][1])
            t_y.append(y)

#                if p_y[0] == '+1' and y == '+1':
#                    tp += 1
#                elif p_y[0] == '+1' and y == '-1':
#                    fp += 1
#                elif p_y[0] == '-1' and y == '-1':
#                    tn += 1
#                elif p_y[0] == '-1' and y == '+1':
#                    fn += 1
        else:
            X.append(x)
            Y.append(y)

        if count == int(text_count / 5):
            LR_model.fit(X, Y)
            test_flag = True
lw = 2
precision, recall, th = precision_recall_curve(np.array(t_y), np.array(p_y))
plt.clf()
plt.plot(recall, precision, lw=lw, color='navy',
         label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.show()



#        accuracy = (tp + tn) / (tp + tn + fp + fn)
#        precision = tp / (fp + tp)
#        recall = tp / (tp + fn)
#        F_measure = 2 * precision * recall / (precision + recall)
#        print('正解率：{}\n適合率：{}\n再現率：{}\nF1スコア：{}' .format(accuracy, precision, recall, F_measure))
