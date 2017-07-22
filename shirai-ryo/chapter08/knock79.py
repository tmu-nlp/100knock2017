import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt

y_scores = pickle.load(open( "predicted.pickle", "rb" ))
y_true = pickle.load(open( "expected.pickle", "rb" ))
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
plt.plot(precision, recall)
plt.title('適合率 - 再現率')
plt.xlabel('適合率')
plt.ylabel('再現率')
plt.show()
