import numpy as np
#from sklearn import cross_validation
from knock72 import word_id,pn_list
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from knock77 import confmat_status
import pickle

with open('word_ids.pkl','rb') as ids:
    word_ids = pickle.load(ids)


def descrive(id_list,pn_list):
  precision, recall, th = precision_recall_curve(np.array(id_list), np.array(pn_list))
  plt.clf()
  plt.plot(recall, precision, lw=2, color='navy',label='Precision-Recall curve')
  plt.xlabel('Recall')
  plt.ylabel('Precision')
  plt.ylim([0.0, 1.05])
  plt.xlim([0.0, 1.0])
  plt.show()

#k_fold = cross_validation.KFold(n = len(pn_list),n_folds = 5)
k_fold = 5

word_id = np.array(word_id)
pn_list = np.array(pn_list)
#print(pn_list)

def make_list(list_):
    a_list = []
    b_list = []
    counter = 0
    for i in range(len(list_)):
        a_list.append(list_[i])
        if counter >= (len(list_) / k_fold) or i == len(list_)-1:
            counter = 0
            b_list.append(a_list)
            a_list = []
        counter += 1
    return b_list
#print(np.shape(pn_list_tr[0]))
score_list = []

if __name__ == '__main__':
    for i in range(k_fold):
        lr = LogisticRegression()
        id_train = []
        pn_train = []
        word_id_tr = make_list(word_id)
        pn_list_tr = make_list(pn_list)
        id_test = word_id_tr[i]
        pn_test = pn_list_tr[i]
        del word_id_tr[i]
        del pn_list_tr[i]
#        print(len(pn_test))
        for ii in range(len(word_id_tr)):
            for jj in range(len(word_id_tr[ii])):
#                print(word_id_tr[ii][jj])
                id_train.append(word_id_tr[ii][jj])
                pn_train.append(pn_list_tr[ii][jj])
#        print(np.shape(id_train),np.shape(pn_train))
        #id_train = list(map(list,zip(*id_train)))
        #pn_train = list(map(list,zip(pn_train)))
    #    lr.fit(id_train,pn_train)

        score_list = []
        for line in id_test:
            score_list.append(lr.predict(line)[0])
        descrive(id_test,score_list)
