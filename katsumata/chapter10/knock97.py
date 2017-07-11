import numpy as np
from sklearn.cluster import KMeans
import pickle

if __name__ == '__main__':
    country_name = dict()
    cls = KMeans(n_clusters=5)
    with open('country_vec.dump', 'rb') as feat_f:
        country_dict = pickle.load(feat_f)
    for id_num, item in enumerate(country_dict.items()):
        country_name[item[0]] = id_num 
        if id_num == 0:
            country_mat = item[1]
            continue
        country_mat = np.vstack((country_mat, item[1]))
    with open('kmeans.dump', 'wb') as o_f:
        pickle.dump((country_name, cls.fit_predict(country_mat)), o_f)
    cls.fit_predict(country_mat)
    labels = cls.labels_
    country_label = dict()
    print ('とりあえず出力')
    for item, label in zip(country_name, labels):
        print ('{}\t{}'.format(label, item))
        country_label[item] = int(label)

    print ('ソートしたやつ')
    for key, value in sorted(country_label.items() , key=lambda x:x[1]):
        print ('{}\t{}'.format(value, key))
