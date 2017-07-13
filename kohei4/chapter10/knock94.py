"""
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．

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
    input_file = './wordsim353/combined.tab'
    output_file = '94_output.txt'

    t_i = get_t_i_c_i(knock84_outputfile)
    dec_MT_X = Get_decomposedMT_X(decomposed_file)
    #np.shape(dec_MT_X)

    """
    #norm = np.linalg.norm(dec_MT_X, ord=2, axis=1)
    #norm_X = dec_MT_X / norm[ :, np.newaxis]
    #print(t_i)
    #print(t_c)

    """
    with open(input_file, 'rt') as ff,\
    open(output_file, 'wt') as gg:
        for i, line in enumerate(ff):
            #if i >= 0 and i <= 6:
                if i  == 0:
                    line = line.strip() +  '\tWordn2Vec'
                    print(line, file=gg)

                else:
                    try:
                        col = line.strip().split('\t')
                        #print(col[0],col[1])
                        cos_s = cos_sim(dec_MT_X[t_i[col[0]]],dec_MT_X[t_i[col[1]]])

                    except KeyError:
                        keys_index = 'Unknown-Word'
                        cos_s = -1

                    print('{}\t{}'.format(line.strip(),cos_s),file = gg)



                #n_line = line[:] + [keys[index],cos_s]
                #print(*n_line)
