"""
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．


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


def get_MT_X(file):

    with open(file, 'rb') as ff:
        MT_X = pickle.load(ff)
    return MT_X

def get_t_i_c_i(file):

    with open(file, 'rb') as ff:
        t_i,c_i = pickle.load(ff)
    return t_i, c_i



    #print(country)

if __name__ == "__main__":

    f_t_c_file = '80corpus_f_t_c_'
    knock84_outputfile = 'knock84_out'
    knock84_outputfile2 = 'knock84_out_2'
    #decomposed_file = 'decomposed_100'
    #decomposed_file = 'decomposed_100_ARPACK'
    decomposed_file = 'decomposed_300'
    t_i, c_i = get_t_i_c_i(knock84_outputfile)

    MT_X = get_MT_X(knock84_outputfile2)

    #print(t_i)
    #print(t_c)
    #print(np.shape(MT_X))

    #decompression
    #clf = sklearn.decomposition.TruncatedSVD(100,algorithm = 'arpack')
    clf = sklearn.decomposition.TruncatedSVD(300)
    decomposed = clf.fit_transform(MT_X)
    #io.savemat(decompressed_file, {'decompressed_100': decompressed})

    with open(decomposed_file,'wb') as ff:
        pickle.dump(decomposed,ff)




    #lsprint(Mat_X, np.shape(Mat_X))
    #with open(knock84_outputfile, 'wb') as gg:
    #    pickle.dump([t_i,c_i],gg)
    #with open(knock84_outputfile2, 'wb') as hh:
    #    pickle.dump(Mat_X, hh)
