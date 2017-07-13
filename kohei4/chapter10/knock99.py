"""
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
"""
import bz2
import re
from sklearn import cluster as cl
from collections import Counter, OrderedDict
from collections import defaultdict
import pickle
import numpy as np
import math
import scipy
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

def Get_MT_X(file):

    with open(file, 'rb') as ff:
        MT_X = pickle.load(ff)
    return MT_X

def get_t_i(file):

    with open(file, 'rb') as ff:
        t_i = pickle.load(ff)
    return t_i



def getcountry(file_name):
    with open(file_name,'r') as ff:
        country_l = []
        for ii, line in enumerate(ff):
            if (ii % 2) == 1:
                if ' ' in line.strip():
                    line2 = line.replace(' ', '_', 100)
                    country_l.append(line2.strip())
                else:
                    country_l.append(line.strip())
    return country_l
    #print(country)

if __name__ == "__main__":

    #country_l = getcountry('../chapter09/countries2.tsv')

    index_file = 'country_idx'
    ntx_file = 'country_MTX'

    MT_X = Get_MT_X(ntx_file)
    t_i = get_t_i(index_file)
    TSNE_2 = TSNE(n_components=2,perplexity=41, learning_rate=300,\
    random_state=0,n_iter=2000).fit_transform(MT_X)
    cluster = cl.KMeans(n_clusters = 5,random_state=0).fit_predict(MT_X)
    #print(TSNE_2)
    #print(cluster)
    data_l = []
    for i in(range(len(cluster))):
        data_l.append([TSNE_2[i,0],TSNE_2[i,1],cluster[i]])
    #print(data_l)
    #print(X_reduced[:, 0], X_reduced[:, 1])
    for x, y, c in data_l:
        plt.scatter(x, y, c=c, cmap = 'Set1',vmin=0,vmax=4 )
    plt.show()
    #plt.colorbar()
