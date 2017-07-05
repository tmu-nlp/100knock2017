from knock73 import feature_vector, feature
from sklearn.externals import joblib

feature_list = []
for word in open('knock72_file.txt'):
    word = word.strip().split()[0]
    feature_list.append(word)

LR = joblib.load('LR.pkl')

weight_dict = dict()
for word, weight in zip(feature_list, LR.coef_[0]):
    weight_dict[word] = weight

print('best 10')
for key, value in sorted(weight_dict.items(),key = lambda x:x[1], reverse = True)[:10]:
    print(key, value)

print('\nworst 10') 
for key, value in sorted(weight_dict.items(),key = lambda x:x[1])[:10]:
    print(key, value)
