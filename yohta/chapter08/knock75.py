from sklearn.externals import joblib
from collections import defaultdict
import pickle

lr = joblib.load('lr.pkl')
with open('word_ids.pkl','rb') as id_f:
    word_ids = pickle.load(id_f)

dict_reversed = {}
for key,value in word_ids.items():
    dict_reversed[value] = key
#print(lr.coef_)
word_weight = {}
for word_id,weight in enumerate(lr.coef_[0]): # coef_ = 推定値
    word_weight[dict_reversed[word_id]] = weight

sorted_dict = sorted(word_weight.items(), key = lambda x:x[1],reverse = True)
#print(sorted_dict[:10])
if __name__ == '__main__':
    counter_1 = 0
    print('\nhigh_weight_rank')
    for word,weight in sorted_dict[:10]:
        counter_1 += 1
        print('{}  :\t{}  :\t{}'.format(counter_1,word,weight))
    counter_2 = 0
    print('\nlow_weight_rank')
    for word,weight in sorted_dict[:-11:-1]:
        counter_2 += 1
        print('{}  :\t{}  :\t{}'.format(counter_2,word,weight))
