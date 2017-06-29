import pickle
import numpy as np
import random
from collections import defaultdict

def predict_one(w, phi, th):
    score = 0
    for name, value in phi.items():
        if name in w:
            score += value*w[name]
    e = np.exp(score) 
    if e/(1+e) >=th :
        return 1, e/(1+e)
    else:
        return -1, e/(1+e)
def update_weights(w, phi, y):
    for name, value in phi.items():
        w[name] += int(value)*y

if __name__ == '__main__':
    with open('features.dump', 'rb') as i_f:
        #featureList:tag,sentence,feature
        feature_list = pickle.load(i_f)
    w = defaultdict(int)
    l = 10
    th = .5
    for i in range(l):
        random.shuffle(feature_list)
        for y, x, phi in feature_list:
            y_, prob = predict_one(w, phi, th)
            if y_ != int(y):
                update_weights(w, phi, int(y))
    with open('weight.dump', 'wb') as o_f:
        pickle.dump(dict(w), o_f)
