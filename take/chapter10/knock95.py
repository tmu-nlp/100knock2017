'''
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ
'''

from scipy.stats import pearsonr
import numpy as np
from collections import defaultdict

target_file = 'out94.model90'

x = list()
y = list()

model_a = defaultdict(float)
model_b = defaultdict(float)

with open(target_file) as f:
    for l in f:
        _x = l.strip().split('\t')
        if _x[3] == 'N/A':
            continue
        model_a[_x[0],_x[1]] = _x[2]
        model_b[_x[0],_x[1]] = _x[3]

        # print('{} {}'.format(_x[2], _x[3]))

from pprint import pprint
# pprint(model_a)
# pprint(model_b)

sorted_a = dict()
sorted_b = dict()

#それぞれを降順sortしたときの順位をリストにする

for rank, (k,v) in enumerate(sorted(model_a.items(), key=lambda x:x[1])):
    # print('{}\t{}'.format(k,rank))
    sorted_a[k] = rank

for rank, (k,v) in enumerate(sorted(model_b.items(), key=lambda x:x[1])):
    # print('{}\t{}'.format(k,rank))
    sorted_b[k] = rank


for k_a, v_a in sorted_a.items():
    # print(k_a, v_a)
    x.append(v_a)
    y.append(sorted_b[k_a])

# for a, b in zip(x,y):
#     print('{} {}'.format(a,b))

# r, p = pearsonr(np.array(x), np.array(y))
r, p = pearsonr(x, y)
print('r={}\np={}'.format(r,p))
