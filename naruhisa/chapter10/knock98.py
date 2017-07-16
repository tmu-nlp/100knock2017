from scipy.cluster.hierarchy import ward, dendrogram
import pickle
import matplotlib.pyplot as plt

if __name__ == '__main__':
    vec_list = list()
    c_list = list()
    with open('c_vec.pkl', 'rb') as f:
        c_vec = pickle.load(f)
    for k, v in c_vec.items():
        vec_list.append(v)
        c_list.append(k)
    cluster = ward(vec_list)
    dendrogram(cluster, labels = c_list)
    plt.show()
