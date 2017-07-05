from sklearn.linear_model import LogisticRegression
import pickle

if __name__ == "__main__":
    model = pickle.load(open( "LRmodel.pickle", "rb" ))
    # print(model)
    coef = model.coef_[0] # array[[...]] -> array[0] = []
    coef_asc = sorted(enumerate(coef), key=lambda x: x[1])
    for index, weight in enumerate(coef_asc[:10]):
        print("重み高いトップ{} {}".format(index+1,weight))
    print() #高いのと低いのがくっついてると見難かったので改行を入れただけ
    for index, weight in enumerate(coef_asc[-10:]):
        print("重み低いトップ{} {}".format(index+1,weight))
