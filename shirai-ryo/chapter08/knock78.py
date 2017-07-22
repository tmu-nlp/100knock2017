from sklearn.model_selection import KFold
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import pickle
import numpy as np

features,labels,vectors = pickle.load(open( "data.pickle", "rb" ))
X = np.array(vectors)
y = np.array(labels)
logistic = LogisticRegression()
N = 5
kf = KFold(n_splits=N)
for train_index, test_index in kf.split(X):
    #print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model = logistic.fit(X_train, y_train)
    predicted = model.predict(X_test)
    print(metrics.classification_report(y_test, predicted))
    expected_filename = "expected_k{}.pickle".format(cnt)
    predicted_filename = "predicted_k{}.pickle".format(cnt)
    pickle.dump(y_test, open(expected_filename, "wb" ) )
    pickle.dump(predicted, open(predicted_filename, "wb" ) )

#shortcut
# scores = cross_val_score(logistic, vectors, labels, cv=N)
# print(scores)
