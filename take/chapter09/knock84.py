'''
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列XXを作成せよ．ただし，行列XXの各要素XtcXtcは次のように定義する．

f(t,c)≥10f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}Xtc=PPMI(t,c)=max{log⁡N×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10f(t,c)<10ならば，Xtc=0Xtc=0
ここで，PPMI(t,c)PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．なお，行列XXの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．幸い，行列XXのほとんどの要素は00になるので，非00の要素だけを書き出せばよい．

'''

import dill
import math
from collections import defaultdict
from scipy.sparse import lil_matrix
from scipy import io

with open('f_dist.dill', "rb") as f:
    f_t_c, f_t_star, f_star_c = dill.load(f)

N = len(f_t_c)

#単語t,cのid化
# key = 単語、value:id
ids_t = defaultdict(lambda: len(ids_t))
ids_c = defaultdict(lambda: len(ids_c))
for k, _ in f_t_c.items():
    ids_t[k.split("|_")[0]]
    ids_c[k.split("|_")[1]]

# 単語文脈行列は疎行列なのでこれつかった。行列各成分はインスタンス化時に0.初期化
X_tc_mat = lil_matrix((len(ids_t), len(ids_c)))

#k:単語|_文脈語, v:共起回数、
for k,v in f_t_c.items():
    t, c = k.split("|_")[0], k.split("|_")[1]
    if v >= 10:
        ppmi = max(math.log10(N * v/ (f_t_star[t] * f_star_c[c])), 0)
        X_tc_mat[ids_t[t], ids_c[c]] = ppmi

# 単語文脈行列を書き出す
io.savemat("Xtc", {"Xtc": X_tc_mat})

# あとで単語から単語idひくため
with open('ids_t.dill', 'wb') as f:
    dill.dump(ids_t, f)