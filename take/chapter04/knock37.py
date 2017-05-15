alllist = []
s_list = []  # 一文を構成する形態素のマップを要素にもつリスト

from collections import defaultdict
from collections import Counter

wordscounter = defaultdict(lambda:0)
a = Counter()

with open('neko.txt.mecab') as f:
    for line in f:
        if line == 'EOS\n':
            if len(s_list) > 0:
                alllist.append(s_list.copy())
                s_list.clear()
            continue
        d = {k: v for k, v in [f.split(":") for f in line.rstrip("\n").split(",")]}  # 一文を構成する各形態素のマップ
        s_list.append(d)
        wordscounter[d['base']] += 1
        a[d['base']] += 1

#Solution for prob.37
print(a.most_common(10))
print(dict(a))

a_dict_10 = dict(a.most_common(10))

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'IPAexGothic'

print(sum(a.values())) #206338

x = range(len(a_dict_10))
xlabel = list(a_dict_10.keys())
# y = list(map(lambda x:x/sum(a.values()) ,list(a_dict_10.values())))
y = list(a_dict_10.values())
plt.xticks(x, xlabel)
plt.title('knock37')
plt.xlabel('単語')
plt.ylabel('頻度')
plt.bar(x,y, align='center', width=0.5)
plt.savefig('fig37.png')
plt.show()
