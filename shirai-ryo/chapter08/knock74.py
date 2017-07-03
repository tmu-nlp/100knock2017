from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# 真のラベルと推定されたラベルを引数に与えれば、結果を計算してくれます。
import pickle

if __name__ == "__main__":
    features, labels, vectors = pickle.load(open( "data.pickle", "rb" ))
    model = pickle.load(open( "LRmodel.pickle", "rb" ))
    expected = labels
    predicted = model.predict(vectors)
    pickle.dump(expected, open("expected.pickle", "wb" ) )
    pickle.dump(predicted, open("predicted.pickle", "wb" ) )

    print(confusion_matrix(expected, predicted))

    """
    [[5205  126]
    [ 150 5181]]
    """
