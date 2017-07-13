"""
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5k=5として実行せよ．
"""
import bz2
import re
from sklearn import cluster as cl
from collections import Counter, OrderedDict
from collections import defaultdict
import pickle
import numpy as np
import math

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

    cluster = cl.KMeans(n_clusters = 5).fit_predict(MT_X)
    #print(cluster)
    #print(t_i.keys())

    result = zip(t_i.keys(), cluster)
    #print(*result)

    for cty, cat in sorted(result, key= lambda x: x[1]):
        print('{}\t{}'.format(cat, cty))
