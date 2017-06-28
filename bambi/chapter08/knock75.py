from sklearn.linear_model import LogisticRegression
import pickle
if __name__ == '__main__':
    model = pickle.load(open( "LR_model.pickle", "rb" ))
    coef = model.coef_[0]# array[[...]] -> array[0] = []
    coef_asc = sorted(enumerate(coef), key=lambda x: x[1])
    for index, weight in enumerate(coef_asc[:10]):
        print("top{} {}".format(index,weight))
    for index, weight in enumerate(coef_asc[-10:]):
        print("bottom{} {}".format(index,weight))
