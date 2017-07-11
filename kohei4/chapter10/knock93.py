"""
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
"""

import numpy as np
import math

def eval(file):

    file = file

    NN = 0
    Correct = 0
    Unknown = 0
    with open(file, 'rt') as ff:
        for line in ff:
            NN += 1
            cols = line.strip().split(' ')
            #print(cols[0],cols[1],cols[2],cols[3],cols[4],cols[5])
            if cols[3] == cols[4]:
                Correct += 1
            if cols[5] == '-1':
                Unknown += 1
        return Correct, NN, Unknown




    #print(country)

if __name__ == "__main__":
    input_file_90 = '92_output.txt'
    input_file_85 = '92_output_2.txt'
    input_file_85_100 = '92_output_3.txt'

    C1, N1, U1 = eval(input_file_90)
    #print(C1,N1,U1)
    C2, N2, U2 = eval(input_file_85)
    C3, N3, U3 = eval(input_file_85_100)


    print('Word2Vec: Total Accuracy: {}, Accuracy witout Unknown: {} '\
    .format(C1/N1, C1/(N1 - U1) ))

    print('Knock85 Model: Total Accuracy: {}, Accuracy witout Unknown: {} '\
    .format(C2/N2, C2/(N2 - U2) ))

    print('Knock85_100 Model: Total Accuracy: {}, Accuracy witout Unknown: {} '\
    .format(C3/N3, C3/(N3 - U3) ))
