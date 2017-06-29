import random

# filename = 'rt-polarity.pos'
filename = 'concat.txt'
shuffled = 'sentiment.txt'
# with open(filename, encoding='utf-8', errors='ignore') as f:
sentence_list = []
p=0
n=0
with open(filename, encoding="latin-1") as f:#utf-8だと4700バイトあたりでロード失敗する
    for l in f:
        """問題文の指示どおり、まずはシャッフルして、それぞれの極性の文数を数える"""
        sentence_list.append(l) #改行コードを削除してメモリに展開

random.shuffle(sentence_list)

with open(shuffled,'w') as f:
    for l in sentence_list:
        f.write(l)
        # 一行の構造は、行頭に極性、スペースを開けて文が始まる。\
        # splitしてリストの先頭要素を取り出しintへキャストして正負(極性)を判定
        x = int(l.split(' ')[0])
        if x > 0:
            p += 1
        else:
            n += 1

print('pos-> {} , neg -> {}'.format(p,n))
