"""
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．

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

def cos_sim(v1, v2):
    #print(v1,v2)
    #print(np.dot(v1, v2))
    #print(np.linalg.norm(v1),np.linalg.norm(v2))
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


    #print(country)

if __name__ == "__main__":

    f_t_c_file = '80corpus_f_t_c_'
    knock84_outputfile = 'knock84_out'
    knock84_outputfile2 = 'knock84_out_2'
    decomposed_file = 'decomposed_100'
    #decomposed_file = 'decomposed_300'
    target_word1 = 'United_States'
    target_word2 = 'U.S'
    target_word3 = 'United_States_of_America'
    target_word4 = 'Republic_of_Korea'
    target_word5 = 'United_Kingdom'

    t_i, c_i = get_t_i_c_i(knock84_outputfile)

    dec_MT_X = Get_decomposedMT_X(decomposed_file)

    #print(t_i)
    #print(t_c)
    print('Decomposed Mtx Shape =',np.shape(dec_MT_X))

    print('Target Words = ',target_word1, target_word2)
    print('IDX = ', t_i[target_word1], t_i[target_word2])
    print('cos類似度 = ', cos_sim(dec_MT_X[t_i[target_word1]], dec_MT_X[t_i[target_word2]]))

    print('Target Words = ',target_word1, target_word3)
    print('IDX = ', t_i[target_word1], t_i[target_word3])
    print('cos類似度 = ', cos_sim(dec_MT_X[t_i[target_word1]], dec_MT_X[t_i[target_word3]]))

    print('Target Words = ',target_word1, target_word4)
    print('IDX = ', t_i[target_word1], t_i[target_word4])
    print('cos類似度 = ', cos_sim(dec_MT_X[t_i[target_word1]], dec_MT_X[t_i[target_word4]]))

    print('Target Words = ',target_word1, target_word5)
    print('IDX = ', t_i[target_word1], t_i[target_word5])
    print('cos類似度 = ', cos_sim(dec_MT_X[t_i[target_word1]], dec_MT_X[t_i[target_word5]]))


    #lsprint(Mat_X, np.shape(Mat_X))
    #with open(knock84_outputfile, 'wb') as gg:
    #    pickle.dump([t_i,c_i],gg)
    #with open(knock84_outputfile2, 'wb') as hh:
    #    pickle.dump(Mat_X, hh)
