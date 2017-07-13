from sklearn.manifold import TSNE
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
    cluster = TSNE().fit_transform(vec_list)
    plt.scatter(cluster[:, 0], cluster[:, 1])
    for s,x,y in zip(c_list,cluster[:,0], cluster[:,1]):
        plt.annotate(s, xy=(x,y))
    plt.show()
