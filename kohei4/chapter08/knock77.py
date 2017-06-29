"""
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，
F1スコアを求めるプログラムを作成せよ．

正例に関するF1スコア

黒橋本　146ページ

"""

import sys
import math
from collections import defaultdict
from stemming.porter2 import stem

result_file = '76.txt'
def check_f(result_file):
# 結果を読み込んで集計
    TrPo = 0      #   予想が+1、正解も+1
    FaPo = 0      #   予想が+1、正解は-1
    FaNe = 0      #   予想が-1、正解は+1
    TrNe = 0      #   予想が-1、正解も-1


    with open(result_file) as gg:
        for line in gg:
            flag = line.split('\t')
            #print(cols)

            if flag[0].strip() == '1':         # label
                if flag[1].strip() == '1':     # predicted
                    TrPo += 1
                elif flag[1].strip() == '-1':
                    FaNe += 1
            elif flag[0].strip() == '-1':
                if flag[1].strip() == '1':
                    FaPo += 1
                elif flag[1].strip() == '-1':
                    TrNe += 1


    accuracy = (TrPo + TrNe) / (TrPo + FaPo + FaNe + TrNe)
    precision = TrPo / (TrPo + FaPo)
    recall = TrPo / (TrPo + FaNe)
    f_m = (2 * recall * precision) / (recall + precision)

    return accuracy, precision, recall, f_m


# スコア算出
accuracy, precision, recall, f_m = check_f(result_file)
print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
    accuracy, precision, recall, f_m))
