from sklearn.linear_model import LogisticRegression
import pickle
from sklearn import metrics
if __name__ == '__main__':
    expected = pickle.load(open( "expected.pickle", "rb" ))
    predicted = pickle.load(open( "predicted.pickle", "rb" ))
    column_names = ['-1: negative', '1: positive']
    print(metrics.classification_report(expected, predicted, target_names=column_names))
