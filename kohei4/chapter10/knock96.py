"""
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
"""
import bz2
import re
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

    input_file = 'country_list90.txt'
    index_file = 'idx_wordvec'
    ntx_file = 'wordvecMTX'
    mtxout = 'country_MTX'
    idxout = 'country_idx'

    country_l=[]
    with open(input_file, 'r') as ff:
        for line in ff:
            country_l.append(line.strip())

    MT_X = Get_MT_X(ntx_file)
    t_i = get_t_i(index_file)

    n_t_i = OrderedDict()
    MT_X_new = np.empty([0,300], dtype = np.float64)
    cnt = 0
    no_reg = 0
    for line in country_l:
        try:
            country = line.strip()
            index = t_i[country]
            MT_X_new = np.vstack([MT_X_new, MT_X[index]])
            n_t_i[country] = cnt
            cnt += 1
        except:
            no_reg += 1
            pass
    print("Reg_Country = ", cnt, "Not Found = ", no_reg)

    with open(mtxout, 'wb') as ff:
        pickle.dump(MT_X_new,ff)
    with open(idxout, 'wb') as ff:
        pickle.dump(n_t_i, ff)

    #print(country_l)
    #country_s = set(country_l)
    #print(country_s)
