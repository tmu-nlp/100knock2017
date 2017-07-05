from sklearn.linear_model import LogisticRegression
import pickle
# from sklearn import metrics
from sklearn.metrics import classification_report

if __name__ == "__main__":
    expected = pickle.load(open( "expected.pickle", "rb" ))
    predicted = pickle.load(open( "predicted.pickle", "rb" ))
    print(classification_report(expected, predicted))

    # 参考 http://nonbiri-tereka.hatenablog.com/entry/2014/08/07/100152
    # column_names = ['-1: negative', '1: positive'] をしておいて
    # (classification_report(expected, predicted, target_names=column_names)) で名前を変えられる
