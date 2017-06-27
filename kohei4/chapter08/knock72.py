'''
本章では，Bo Pang氏とLillian Lee氏が公開しているMovie Review Dataのsentence
polarity dataset v1.0を用い，文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に
分類するタスク（極性分析）に取り組む．

72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが
最低限のベースラインとなるであろう．

秋山メモ
どこから、STOPリストを取ろうかと悩んだ。対象の文書から大量に出てくるものを
とっても良いし、すでにあるものでも良いし。
フランス語も入っているし。で、オラクルのストップワードというのがあったので、
そこでの英語とフランス語を合わせたリストを使った。
フランス語は、活用形（？）が沢山あるので、大変。


'''
# coding: utf-8
#from collections import defaultdict

import re
import codecs
import random
from stemming.porter2 import stem
from collections import Counter



def stop_check(word):
    stop_file = open('stop_e_f.txt', 'r')
    with stop_file:
        stop_list = [ line.strip() for line in stop_file]
    if word in stop_list:
        return True
    else:
        return False

inputfile = 'sentiment.txt'
feature = 'featureset.txt'

w_count = Counter()
with open(inputfile,'r') as ff, open(feature,'w') as gg:
    for line in ff:

        for word in line[3:].split(' '):
            word = word.strip()

            #if stop_check(word):
                #print('Stopword !! = ',word)
                #continue

            if word != '!' and word != '?' and len(word) <= 1:
                continue

            word = stem(word)
            if stop_check(word):
                #print('Stopword !! = ',word)
                continue

            w_count.update([word])

    feature = [word for word, count in w_count.items() if count >= 6 ]
    print(*feature, sep='\n', file = gg)


#word = input('Enter a check word: ')
#print(stop_check(word))
