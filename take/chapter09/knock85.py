'''
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ
'''

from scipy import io
import sklearn.decomposition

Xtc = io.loadmat('Xtc')['Xtc']

dimen = 150
svd = sklearn.decomposition.TruncatedSVD(dimen)
svded = svd.fit_transform(Xtc)
io.savemat('Xtc_' + str(dimen), {'Xtc_' + str(dimen): svded})