from sklearn.linear_model import LogisticRegression
import pickle
from sklearn import metrics

if __name__ == "__main__":
    features,labels,vectors = pickle.load(open( "data.pickle", "rb"))
    model = pickle.load(open( "LRmodel.pickle", "rb"))
    predicted = model.predict(vectors)
    prob = model.predict_proba(vectors)
    for x, y, z in zip(predicted, labels, prob):
        print("{}\t{}\t{}".format(x, y, max(z)))
