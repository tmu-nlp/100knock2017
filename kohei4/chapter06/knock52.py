"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""
# coding: utf-8
#from collections import defaultdict
from stemming.porter2 import stem
import re


input_file = 'nlp.txt'

def input_f_word():

    with open(input_file) as lines:

        #ptn = re.compile(r'(.*?[\.|\:|\?|\!])(\s)([A-Z].*)')

        for line in lines:
            l_word=[]
            line = line.strip()

            l_word = line.split()
            for word in l_word:
                word = re.sub(r"(\,|\.|\(|\)|\'|\"|)",'',word)
                "Need to handle '? -' ?"
                print('{}\t{}'.format(word,stem(word)))

            #print()

input_f_word()
