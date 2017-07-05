"""
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") +
vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．


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
    if (np.linalg.norm(v1) * np.linalg.norm(v2)) == 0:
        return -1

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


    #print(country)

if __name__ == "__main__":

    f_t_c_file = '80corpus_f_t_c_'
    knock84_outputfile = 'knock84_out'
    knock84_outputfile2 = 'knock84_out_2'
    decomposed_file = 'decomposed_100'
    #decomposed_file = 'decomposed_300_ARPACK'
    #decomposed_file = 'decomposed_300'
    target_word1 = 'United_States'
    target_word2 = 'U.S'
    target_word3 = 'United_States_of_America'
    target_word4 = 'Republic_of_Korea'
    target_word5 = 'United_Kingdom'
    target_word6 = 'Japan'
    target_word7 = 'Spain'
    target_word8 = 'Madrid'
    target_word9 = 'Athens'



    t_i, t_c = get_t_i_c_i(knock84_outputfile)

    dec_MT_X = Get_decomposedMT_X(decomposed_file)
    #np.shape(dec_MT_X)

    """
    #norm = np.linalg.norm(dec_MT_X, ord=2, axis=1)
    #norm_X = dec_MT_X / norm[ :, np.newaxis]
    #print(t_i)
    #print(t_c)
    print('Decomposed Mtx Shape =',np.shape(dec_MT_X))
    print('Target Words = ',target_word1, target_word2)
    print('IDX = ', t_i[target_word1], t_i[target_word2])
    print('cos類似度 = ', cos_sim(dec_MT_X[t_i[target_word1]], dec_MT_X[t_i[target_word2]]))
    print('cos類似度(norm_X) = ', np.dot(norm_X[t_i[target_word1]], norm_X[t_i[target_word2]]))
    print('Target Words = ',target_word1, target_word4)
    print('IDX = ', t_i[target_word1], t_i[target_word4])
    print('cos類似度 = ', cos_sim(dec_MT_X[t_i[target_word1]], dec_MT_X[t_i[target_word4]]))
    print('cos類似度(norm_X) = ', np.dot(norm_X[t_i[target_word1]], norm_X[t_i[target_word4]]))
    """

    synth_vec = dec_MT_X[t_i[target_word7]] - dec_MT_X[t_i[target_word8]] + dec_MT_X[t_i[target_word9]]
    print(len(t_i))
    cos_list=[]
    for ii in range(len(t_i)):
        cos_list.append([ii,cos_sim(dec_MT_X[ii],synth_vec)])

    #print(sorted(cos_list,reverse=True)[:10])

    cos_list.sort(reverse=True,key = lambda x: x[1])
    keys = list(t_i.keys())
    #print(cos_list[:10])
    for index, cos_s in cos_list[:20]:
        print('{}\t{}'.format(keys[index], cos_s))
