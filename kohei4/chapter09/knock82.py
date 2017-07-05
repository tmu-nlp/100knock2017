"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語ttに関して，単語ttと文脈語ccのペアをタブ区切り形式
ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

ある単語ttの前後dd単語を文脈語ccとして抽出する（ただし，文脈語に単語ttそのものは含まない）
単語ttを選ぶ度に，文脈幅ddは{1,2,3,4,5}{1,2,3,4,5}の範囲でランダムに決める．
"""

import bz2
import re
import random


    #print(country)

if __name__ == "__main__":

    with open('80corpus_edit_country.txt','r') as ff,\
    open('80corpus_context_2.txt','w') as gg:
        for ii, line in enumerate(ff):
            #if ii >= 0 and ii <= 3:
                line_words = [x for x in line.strip().split()]
                #print(len(line_words))
                for j in range(len(line_words)):
                    d = random.randint(1,5)
                    pre = max(j - d, 0)
                    pos = min(j + d + 1, len(line_words))
                    #print(d,pre,pos)
                    for k in range(pre, pos):
                        if j != k:
                            print('{}\t{}'.format(line_words[j],line_words[k]), file=gg)
