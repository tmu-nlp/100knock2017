from sklearn.linear_model import LogisticRegression
import pickle
if __name__ == '__main__':
    features,labels,vectors = pickle.load(open( "data.pickle", "rb" ))
    logistic = LogisticRegression()
    model = logistic.fit(vectors,labels)
    pickle.dump(model, open("LR_model.pickle", "wb" ) )
    print(model)
