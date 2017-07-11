"""
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""
from collections import Counter, OrderedDict
from collections import defaultdict
import pickle
import numpy as np
import math
from scipy import sparse, io
import sklearn.decomposition


def n_spearman(array_a, array_b):
    N = len(array_a)
    return (1 - (6*sum((array_a - array_b)**2)) / float(N**3 - N))

def spearman(list_a, list_b):
    N = len(list_a)
    return 1 - ((6 * sum(map(lambda a, b: (a - b) ** 2,list_a, list_b))) / float(N ** 3 - N) )


    #print(country)

if __name__ == "__main__":

    input_file = '94_output.txt'
    output_file = '95_output.txt'

    with open(input_file, 'rt') as ff,\
    open(output_file, 'wt') as gg:
        word_list = []
        unknown = 0
        for i, line in enumerate(ff):
            #if i >= 0 and i <= 10:
                if i  == 0:
                    line = 'Idx\t' + line.strip() + '\tHuman Order\tW2V Order'
                    #print(line)
                    cols = line.strip().split('\t')
                    word_list.append(cols)

                else:
                    cols = cols = line.strip().split('\t')
                    if cols[3] == '-1':
                        unknown += 1
                    else:
                        word_list.append([i-unknown,*cols])
        #print(word_list)
        #print(unknown)

        sort_list = word_list[1:]
        #print(*sort_list)

        sort_list_1 = sorted(sort_list, key= lambda x: float(x[3]), reverse= True)
        #print(*sort_list_1)

        for i, line in(enumerate(sort_list_1)):
            line.append(i+1)
            #sort_list_1[i].append(i+1)
        #print(sort_list_1)
        sort_list_1 = sorted(sort_list, key= lambda x: float(x[4]), reverse= True)
        for i, line in(enumerate(sort_list_1)):
            line.append(i+1)
            #sort_list_1[i].append(i+1)
        #print(*sort_list_1)
        sort_list_1 = sorted(sort_list, key= lambda x: int(x[0]), reverse= False)
        #print(*sort_list_1)
        order1 = []
        order2 = []
        for line in sort_list_1:
            order1.append(line[5])
            order2.append(line[6])

        ar_order1 = np.array(order1)
        ar_order2 = np.array(order2)

        sp_ra = n_spearman(ar_order1,ar_order2)

        print("Spearman's rank correlation coefficient = ",sp_ra)
        print("Unknown Words = ", unknown)

        with open(output_file,'wt') as ff:
            print("Spearman's rank correlation coefficient = ",sp_ra, file=ff)
            print("Unknown Words = ", unknown, file=ff)
            for line in word_list:
                print(line,file=ff)
