'''
英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを
文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
'''
# coding: utf-8
#from collections import defaultdict

import re

input_file = 'nlp.txt'

def input_f_lines():

    with open(input_file) as lines:

        ptn = re.compile(r'(.*?[\.|\:|\?|\!])(\s)([A-Z].*)')

        for line in lines:
            l_line=[]
            line = line.strip()

            while len(line) > 0:

                m = ptn.search(line)
                #m = re.search(r'(.*?[\.|\:|\?|\!])(\s)([A-Z].*)',line)

                if m:
                    yield m.group(1)
                    line = m.group(3)

                else:
                    yield line
                    line =''
                    break


for line in input_f_lines():
    print(line)
