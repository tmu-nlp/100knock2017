from sklearn.linear_model import LogisticRegression
import pickle
from sklearn import metrics
if __name__ == '__main__':
    features,labels,vectors = pickle.load(open( "data.pickle", "rb" ))
    model = pickle.load(open( "LR_model.pickle", "rb" ))
    predicted = model.predict(vectors)
    prob = model.predict_proba(vectors)
    cnt = 0 # heavy list so, just want to break 
    for x, y, z in zip(predicted,labels,prob):
        print(x,y,max(z)) # max coz got prob as list
        cnt += 1
        if cnt == 10:
            break
