"""
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列XXを作成せよ．ただし，行列XXの各要素XtcXtcは次のように定義する．

f(t,c)≥10f(t,c)≥10ならば，Xtc=PPMI(t,c)=
max{log(N×f(t,c)/f(t,∗)×f(∗,c)),0}
f(t,c)<10ならば，Xtc=0
ここで，PPMI(t,c)PPMI(t,c)はPositive Pointwise Mutual Information
（正の相互情報量）と呼ばれる統計量である．なお，行列XXの行数・列数は数百万オーダとなり，
行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列XXのほとんどの要素は00になるので，非00の要素だけを書き出せばよい．

巨大行列の対策せずに実行すると、killed: 9がでた。メモリ一杯なのかと。
pickel_dumpしないと出ない。
"""

import bz2
import re
import random
from collections import Counter, OrderedDict
from collections import defaultdict
import pickle
import numpy as np
import math
from scipy import sparse, io

X = defaultdict()
t_i = OrderedDict()
c_i = OrderedDict()


def get_f_c(file):

    with open(file, 'rb') as ff:
        set_f_c = pickle.load(ff)
    return set_f_c




    #print(country)

if __name__ == "__main__":


    #f_t_c_file = '80corpus_f_t_c_deb'
    f_t_c_file = '80corpus_f_t_c_'
    knock84_outputfile = 'knock84_out'
    knock84_outputfile2 = 'knock84_out_2'


    set_fc = get_f_c(f_t_c_file)
    f_t_c, f_t_, f__c, NN = set_fc
    #print(len(f_t_c))
    #print(len(f_t_))
    size_t = len(f_t_)
    #print(len(f__c))
    size_c = len(f__c)
    #print(NN)
    for i, key in enumerate(f_t_.keys()):
        t_i[key] = i
    for i, key in enumerate(f__c.keys()):
        c_i[key] = i

    #Mat_X = np.zeros((size_t,size_c))
    Mat_X = sparse.lil_matrix((size_t,size_c))
    #for key in f_t_c.keys():
    #    print(key[0],key[1])
    #print(Mat_X, np.shape(Mat_X))

    for key, ftc in f_t_c.items():
        if ftc >= 10:
            tkn_t = key[0]
            tkn_c = key[1]
            ppmi = max((math.log(NN * ftc)/(f_t_[tkn_t]*f__c[tkn_c])), 0 )
            Mat_X[t_i[tkn_t],c_i[tkn_c]] = ppmi
            #print(ftc,f_t_[tkn_t],f__c[tkn_c],ppmi )
            #if ftc == 10:
                #print(tkn_t, tkn_c)
    #lsprint(Mat_X, np.shape(Mat_X))
    with open(knock84_outputfile, 'wb') as gg:
        pickle.dump([t_i,c_i],gg)
    with open(knock84_outputfile2, 'wb') as hh:
        pickle.dump(Mat_X, hh)
