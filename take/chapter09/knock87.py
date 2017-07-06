'''
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
'''

import numpy as np
from scipy import io
import dill
from collections import defaultdict


Xtc_150 = io.loadmat('Xtc_150')['Xtc_150']

with open('ids_t.dill','rb') as f:
    ids_t = dill.load(f)


def cossim(_a, _b):
    norm_a = np.linalg.norm(_a)
    norm_b = np.linalg.norm(_b)
    return np.dot(_a, _b)/(norm_a * norm_b)


def make_vec(word):
    return Xtc_150[ids_t[word.lower()]]


'''
knock 86
"united_states" 単語埋め込みベクトルを表示せよ
'''
print(' ----- knock86 ----\nunited_states 単語埋め込みベクトルを表示せよ\n')
print(Xtc_150[ids_t["united_states"]])



'''
knock 87
united_states と u.sのcos 類似度を計算せよ
'''
print(' \n----- knock87 ----\nunited_states と u.sのcos類似度\n')
print(cossim(Xtc_150[ids_t["united_states"]], Xtc_150[ids_t["u.s"]]))

import scipy.spatial.distance

usa = np.array(Xtc_150[ids_t["united_states"]])
usb = np.array(Xtc_150[ids_t["u.s"]])

print(type(usa))

score = scipy.spatial.distance(usa, usb)
print('scipy cos: ',score)


'''
knock 88
englandとコサイン類似度が高いトップ１０
'''
print(' \n----- knock88 ----\nenglandとコサイン類似度が高いトップ10\n')
vec_england = Xtc_150[ids_t['england']]
norm_england = np.linalg.norm(vec_england)
top10eng = defaultdict(float)
for k in ids_t.keys():
    if (Xtc_150[ids_t[k]] == 0.0).all():
        continue
    target_norm = np.linalg.norm(Xtc_150[ids_t[k]])
    top10eng[k] = np.dot(vec_england, Xtc_150[ids_t[k]])/(norm_england * target_norm)


from pprint import pprint

pprint(sorted(top10eng.items(), key=lambda x: x[1], reverse=True)[0:10])



'''
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''

# vec_h = (make_vec('king') - make_vec("man") + make_vec("woman"))
vec_h = make_vec('Spain') - make_vec("Madrid") + make_vec("Athens")


norm_h = np.linalg.norm(vec_h)
sim_h_dict = defaultdict(float)
for k in ids_t.keys():
    if (Xtc_150[ids_t[k]] == 0.0).all():
        continue
    target_norm = np.linalg.norm(Xtc_150[ids_t[k]])
    sim_h_dict[k] = np.dot(vec_h, Xtc_150[ids_t[k]])/(norm_h * target_norm)

print(' \n----- knock89 ----\nvec("Spain") - vec("Madrid") + vec("Athens")\n')
pprint(sorted(sim_h_dict.items(), key=lambda x: x[1], reverse=True)[0:10])
