import numpy as np
import pickle
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer

with open('data/answer83','rb') as i_f:
    f_tc,f_t,f_c,N = pickle.load(i_f)
# f_tc : 該当単語と文脈語 カウント
# f_t :　該当単語　カウント
# f_c : 文脈語　カウント

def PPMI(t,c):
    ppmi = np.log2((N * f_tc['{}\t{}'.format(t,c)]) / (f_t[t] * f_c[c]))
    return max(ppmi, 0)

if __name__ == '__main__':
    feature = []
    vector = DictVectorizer()
    dict_ftc_w_c = defaultdict(list)

    for word in f_tc.keys():
        if f_tc[word] < 10:
            continue
        word_,co_ = word.split('\t')
#        print(co_)
        dict_ftc_w_c[word_].append(co_)

    words = dict()
    counter = 0
    for w,c in dict_ftc_w_c.items():
        words[w] = counter
        dict_ = dict()
        for c_ in c:
            dict_[c_] = PPMI(w,c_)
        feature.append(dict_)
        counter += 1

    with open('data/answer84','wb') as o_f:
        pickle.dump((words,vector.fit_transform(feature)),o_f)
