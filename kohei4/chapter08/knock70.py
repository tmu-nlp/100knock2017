'''
本章では，Bo Pang氏とLillian Lee氏が公開しているMovie Review Dataのsentence
polarity dataset v1.0を用い，文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に
分類するタスク（極性分析）に取り組む．

70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに
続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに
続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

Kohei-no-MacBook-Air:chapter08 kohei$ cut -c1-3 sentiment.txt | sort | uniq -c
5331 +1
5331 -1
Kohei-no-MacBook-Air:chapter08 kohei$ wc -l rt-polarity.pos
    5331 rt-polarity.pos
Kohei-no-MacBook-Air:chapter08 kohei$ wc -l rt-polarity.neg
    5331 rt-polarity.neg
Kohei-no-MacBook-Air:chapter08 kohei$


'''
# coding: utf-8
#from collections import defaultdict

import re
import codecs
import random

pos_file = codecs.open('rt-polarity.neg', 'r', 'cp1252')
neg_file = codecs.open('rt-polarity.pos', 'r', 'cp1252')
#senti_file = codecs.open('sentiment.txt', 'w', 'cp1252' )
senti_file = open('sentiment.txt', 'w')

with pos_file, neg_file, senti_file:
    pos = ['+1 '+line for line in pos_file]
    neg = ['-1 '+line for line in neg_file]
    senti = pos + neg

    random.shuffle(senti)

    #[senti_file.writelines(line) for line in senti]
    for line in senti:
        senti_file.writelines(line)

pos_c = 0
neg_c = 0
for line in senti:
    if line[0] == '+':
        pos_c += 1
    elif line[0] == '-':
        neg_c += 1

print('pos = {},  neg = {}'.format(pos_c, neg_c))
