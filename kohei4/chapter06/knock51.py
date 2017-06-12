'''
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
ただし，文の終端では空行を出力せよ．


'''
# coding: utf-8
#from collections import defaultdict

import re

input_file = 'test.txt'

def input_f_word():

    with open(input_file) as lines:

        #ptn = re.compile(r'(.*?[\.|\:|\?|\!])(\s)([A-Z].*)')

        for line in lines:
            l_word=[]
            line = line.strip()

            l_word = line.split()
            for word in l_word:
                print(word)

            print()



input_f_word()
