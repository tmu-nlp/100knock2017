import pickle
import knock74

#入力をりすとにする
def predictFile(f_list, th, w):
    for tag, x, phi in f_list:
        y_, probability = knock74.predict(x.strip(), th, w)
        yield tag, y_, probability
        

if __name__ == '__main__':
    #featureList:tag,sentence,feature
    th = .5
    with open('weight.dump', 'rb') as w_f:
        w = pickle.load(w_f)
    with open('features.dump', 'rb') as i_f:
        feature_list = pickle.load(i_f)
    with open('knock76.txt', 'w') as k_f:
        for t, y_pre, prob in predictFile(feature_list, th, w):
            k_f.write('{}\t{}\t{}\n'.format(t, y_pre, prob))
