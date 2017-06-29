'''
本章では，Bo Pang氏とLillian Lee氏が公開しているMovie Review Dataのsentence
polarity dataset v1.0を用い，文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に
分類するタスク（極性分析）に取り組む．

771. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．


'''
# coding: utf-8
#from collections import defaultdict

import re
import codecs
import random

stop_file = open('stop_e_f.txt', 'r')

def stop_check(word):
    with stop_file:
        stop_list = [ line.strip() for line in stop_file]
    if word in stop_list:
        return True
    else:
        return False


word = input('Enter a check word: ')
print(stop_check(word))
