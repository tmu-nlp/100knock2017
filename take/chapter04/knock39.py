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
        # a[d['base']] += 1

#Solution for prob.36
# for k,v in sorted(dict(wordscounter).items(), key=lambda x:x[1], reverse=True):
#     print(k, v)

# Solution for prob.38
histdict = defaultdict(lambda :0)
#key: 単語出現頻度、value: 単語種類数
for k, v in sorted(dict(wordscounter).items(), key=lambda x: x[1], reverse=True):
    histdict[v] += 1

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'IPAexGothic'

# prob39:Zipf's即
y =list(histdict.keys())
x = range(len(y))
plt.xscale("log")
plt.yscale("log")
plt.title('knock39')
plt.xlabel('単語出現数順位')
plt.ylabel('単語出現頻度')
plt.plot(x,y)
plt.savefig('fig39.png')
plt.show()
