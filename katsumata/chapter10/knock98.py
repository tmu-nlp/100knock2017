from scipy.cluster.hierarchy import dendrogram,ward,leaves_list
import numpy as np
import matplotlib.pyplot as plt
import pickle

if __name__ == '__main__':
    #country_name = dict()
    country_name = list()
    with open('country_vec.dump', 'rb') as feat_f:
        country_dict = pickle.load(feat_f)
    for id_num, item in enumerate(country_dict.items()):
        #country_name[item[0]] = id_num
        country_name.append(item[0])
        if id_num == 0:
            country_mat = item[1]
            continue
        country_mat = np.vstack((country_mat, item[1]))    
    h_cls = ward(country_mat)
    dendrogram(h_cls, labels=country_name)
    plt.show()
