from sklearn.cluster import KMeans
import pickle
import numpy as np

if __name__ == '__main__':
    vec_list = list()

    with open('c_vec.pkl', 'rb') as f:
        c_vec = pickle.load(f)
    for k, v in c_vec.items():
        vec_list.append(v)
    KM = KMeans(n_clusters = 5)
    cluster = KM.fit_predict(vec_list)
    for k, c in zip(c_vec.keys(), cluster):
        print(k, c)
