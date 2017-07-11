"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""
from collections import Counter, OrderedDict
from collections import defaultdict
import pickle
import numpy as np
import math
import sklearn.decomposition
import word2vec

input_file = '80corpus_edit.txt'
word2vec_out = 'word2vec_out.txt'
mtxout = 'wordvecMTX'
idxout = 'idx_wordvec'

word2vec.word2vec(train=input_file, output=word2vec_out, binary= 0,size=300)
"""
85477 300
</s> 0.001334 0.001473 -0.00127
"""

with open(word2vec_out, 'rt') as ff:
    First_line = ff.readline().split(' ')
    dict_size, size_mtx = int(First_line[0]),int(First_line[1])
    print(dict_size, size_mtx)

    idx_word = OrderedDict()
    MT_X = np.zeros([dict_size,size_mtx], dtype= np.float64)

    for i, line in enumerate(ff):
        d_line = line.rstrip().split(' ')
        idx_word[d_line[0]] = i
        #print(d_line[0],len(d_line[1:]))
        MT_X[i] = d_line[1:]

with open(mtxout, 'wb') as ff:
    pickle.dump(MT_X,ff)
with open(idxout, 'wb') as ff:
    pickle.dump(idx_word, ff)
