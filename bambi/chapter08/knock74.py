from sklearn.linear_model import LogisticRegression
import pickle
from sklearn import metrics
if __name__ == '__main__':
    features,labels,vectors = pickle.load(open( "data.pickle", "rb" ))
    model = pickle.load(open( "LR_model.pickle", "rb" ))
    expected = labels
    predicted = model.predict(vectors)
    pickle.dump(expected, open("expected.pickle", "wb" ) )
    pickle.dump(predicted, open("predicted.pickle", "wb" ) )
    print(metrics.confusion_matrix(expected, predicted))
