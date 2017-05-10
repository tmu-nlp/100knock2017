alllist = []
s_list = []  # 一文を構成する形態素のマップを要素にもつリスト

from collections import defaultdict
wordscounter = defaultdict(lambda:0)

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

for k,v in sorted(dict(wordscounter).items(), key=lambda x:x[1], reverse=True):
    # print(k, v/sum(wordscounter.values()))
    print(k, v)

# print(sum(wordscounter.values()))
# print(len(wordscounter))