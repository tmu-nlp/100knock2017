import pickle
from knock72 import *
import knock73

def predict(x, th, w):
    #入力はsentenceを仮定
    phi = create_feature(stemming(excludeStop(x))) 
    tag, prob = knock73.predict_one(w, phi, th)
    return tag, prob 

    
if __name__ == '__main__':
    with open('weight.dump', 'rb') as w_f:
        w = pickle.load(w_f)
    th = .5    
    file_name = 'test.pol'
    with open(file_name) as i_f:
        for line in i_f:
            y_, probability = predict(line.strip(), th, w)
            print ('ラベル {}'.format(y_)) 
            print ('確率 {}'.format(probability))
