import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt
y_scores = pickle.load(open( "predicted_k1.pickle", "rb" ))
y_true = pickle.load(open( "expected_k1.pickle", "rb" ))
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
plt.plot(precision, recall)
plt.title('precision - recall')
plt.xlabel('precision')
plt.ylabel('recall')
plt.show()
