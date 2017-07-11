"""
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．
"""
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
        t_i = pickle.load(ff)
    return t_i

def cos_sim(v1, v2):
    #print(v1,v2)
    #print(np.dot(v1, v2))
    #print(np.linalg.norm(v1),np.linalg.norm(v2))
    if (np.linalg.norm(v1) * np.linalg.norm(v2)) == 0:
        return -1

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


    #print(country)

if __name__ == "__main__":

    knock84_outputfile = 'idx_wordvec'
    decomposed_file = 'wordvecMTX'
    #decomposed_file = 'decomposed_300'
    fami_file = '91_output.txt'
    output_file = '92_output.txt'

    t_i = get_t_i_c_i(knock84_outputfile)
    dec_MT_X = Get_decomposedMT_X(decomposed_file)
    #np.shape(dec_MT_X)

    """
    #norm = np.linalg.norm(dec_MT_X, ord=2, axis=1)
    #norm_X = dec_MT_X / norm[ :, np.newaxis]
    #print(t_i)
    #print(t_c)

    """
    taget_l = []
    with open(fami_file, 'rt') as ff,\
    open(output_file, 'wt') as gg:
        for i, line in enumerate(ff):
            #if i >= 0 and i <= 6:
                try:
                    col = line.strip().split(' ')
                    #print(col)
                    vec_word = dec_MT_X[t_i[col[1]]] \
                    -  dec_MT_X[t_i[col[0]]] \
                    +  dec_MT_X[t_i[col[2]]]
                    #print(len(t_i))
                    cos_list=[]

                    for ii in range(len(t_i)):
                        cos_list.append([ii,cos_sim(dec_MT_X[ii],vec_word)])

                        #print(sorted(cos_list,reverse=True)[:10])

                    cos_list.sort(reverse=True,key = lambda x: x[1])
                    keys = list(t_i.keys())
                    #print(cos_list[:10])
                    index, cos_s = cos_list[0]
                    keys_index = keys[index]


                except KeyError:
                    keys_index = 'Unknown-Word'
                    cos_s = -1


                print('{} {} {}'.format(line.strip(),keys_index,cos_s),file=gg)
                print('{} {} {}'.format(line.strip(),keys_index,cos_s))


                #n_line = line[:] + [keys[index],cos_s]
                #print(*n_line)
