from sklearn.linear_model import LogisticRegression
import pickle

if __name__ == "__main__":
    # data = open("data.pickle", "rb")
    features, labels, vectors = pickle.load(open("data.pickle", "rb"))
    logistic = LogisticRegression()
    model = logistic.fit(vectors, labels)
    pickle.dump(model, open("LRmodel.pickle", "wb"))


"""

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False)

"""
