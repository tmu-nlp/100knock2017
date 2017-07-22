import numpy as np
from sklearn.cluster import KMeans
import pickle

if __name__ == '__main__':
    co_dict = dict()
    cls = KMeans(n_clusters=5)
    with open('data/knock96.dump','rb') as i_f:
        model_dict = pickle.load(i_f)

    for num,item in enumerate(model_dict.items()):
        co_dict[item[0]] = num
        if num == 0:
            mat = item[1]
            continue
        mat = np.vstack((mat,item[1]))

    with open('data/knock97.dump','wb') as o_f:
        pickle.dump((co_dict,cls.fit_predict(mat)),o_f)

    cls.fit_predict(mat)
    labels = cls.labels_
    country_label = dict()
    for key,value in sorted(country_label.items(),key=lambda x:x[1]):
        print ('{}\t{}'.format(value,key))
