from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import pickle

if __name__ == '__main__':
    ids_file = 'feature.ids'
    feature_file = 'sen_list.feature'
    lo = LogisticRegression()

    with open(ids_file,'rb') as ids_data, open(feature_file, 'rb') as fea:
        ids = pickle.load(ids_data)
        features_list, label_list = pickle.load(fea)
    for i in ['accuracy','recall','precision','f1']:
        print('{}:{}'.format(i,cross_val_score(lo, features_list, label_list, cv = 5, scoring=i).mean()))

   
