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
# Solution for prob.38
histdict = defaultdict(lambda :0)
#key: 単語出現頻度、value: 単語種類数
for k, v in sorted(dict(wordscounter).items(), key=lambda x: x[1], reverse=True):
    histdict[v] += 1

#Solution for prob. 38
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'IPAexGothic'

x = range(len(dict(histdict)))
y = list(histdict.values())
xlabel = list(histdict.keys())
plt.xticks(x, xlabel)
plt.title('knock38')
plt.xlabel('出現頻度')
plt.ylabel('単語の種類数')
plt.bar(x,y, align='center', width=0.5)
plt.savefig('fig38.png')
plt.show()
