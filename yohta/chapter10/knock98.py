import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy.cluster.hierarchy import dendrogram,ward,leaves_list

if __name__ == '__main__':
    co_list = list()
    with open('data/knock96.dump', 'rb') as i_f:
        model_dict = pickle.load(i_f)
    for num,item in enumerate(model_dict.items()):
        co_list.append(item[0])
        if num == 0:
            mat = item[1]
            continue
        mat = np.vstack((mat,item[1]))
    h_cls = ward(mat)
    dendrogram(h_cls,labels=co_list)
    plt.show()
