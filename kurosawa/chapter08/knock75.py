import pickle
from collections import defaultdict
from knock72 import make_sentence_feature


if __name__ =='__main__':
    lo_file = 'model.log'
    ids_file = 'feature.ids'
    with open(lo_file, 'rb') as model, open(ids_file, 'rb') as ids_data:
        lo = pickle.load(model)
        ids = pickle.load(ids_data)
    w = lo.coef_[0]
    w_list = defaultdict(float)
    for word,i in sorted(ids.items(), key=lambda x:x[1]):
        w_list[word] = w[i]
    i = 0
    for word, score in sorted(w_list.items(), key=lambda x:x[1],reverse=True):
        if i < 10:
            if i == 0:
                print('<good 10 words>')
            print('\t{}:{}'.format(word,score))
        elif i >= len(w_list)-10:
            if i == len(w_list)-10:
                print('<worse 10 words>')
            print('\t{}:{}'.format(word,score))
        i += 1

