"""
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．

"""

#import bz2
#import re
#import random
from collections import Counter, OrderedDict
from collections import defaultdict
import pickle
import numpy as np
import math
from scipy import sparse, io
import sklearn.decomposition


def Get_decomposedMT_X(file):

    with open(file, 'rb') as ff:
        decom_MT_X = pickle.load(ff)
    return decom_MT_X

def get_t_i_c_i(file):

    with open(file, 'rb') as ff:
        t_i,c_i = pickle.load(ff)
    return t_i, c_i



    #print(country)

if __name__ == "__main__":

    f_t_c_file = '80corpus_f_t_c_'
    knock84_outputfile = 'knock84_out'
    knock84_outputfile2 = 'knock84_out_2'
    decomposed_file = 'decomposed_100'
    target_word = 'United_States'

    t_i, c_i = get_t_i_c_i(knock84_outputfile)

    dec_MT_X = Get_decomposedMT_X(decomposed_file)

    #print(t_i)
    #print(c_i)
    print('Decomposed Mtx Shape =',np.shape(dec_MT_X))

    print('Target Word = ',target_word)
    print(dec_MT_X[t_i[target_word]])


    #lsprint(Mat_X, np.shape(Mat_X))
    #with open(knock84_outputfile, 'wb') as gg:
    #    pickle.dump([t_i,c_i],gg)
    #with open(knock84_outputfile2, 'wb') as hh:
    #    pickle.dump(Mat_X, hh)
