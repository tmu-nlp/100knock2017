import pickle
from sklearn.linear_model import LogisticRegression

def train(sen_list, ids):
    x,y = sen_list    
    lo = LogisticRegression()
    lo.fit(x,y)
    return lo

if __name__ == '__main__':
    sen_list_file = 'sen_list.feature'
    ids_file = 'feature.ids'
    with open(sen_list_file,'rb') as sen_list_data, open(ids_file, 'rb') as ids_data:
        sen_list = pickle.load(sen_list_data)
        ids = pickle.load(ids_data)
    lo_ = train(sen_list, ids)
    with open('model.log', 'wb') as model:
        pickle.dump(lo_, model)
