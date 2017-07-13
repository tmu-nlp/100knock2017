'''
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
'''

# correct = 0
# incorrect = 0
none_cnt = 0

true_of_false = list()

with open('out92') as f:
    for l in f:
        line = l.strip().split()
        print(line)
        true_of_false.append(line[3]==line[4])
        if line[4] == 'none':
            none_cnt += 1
        # if line[3] == line[4]:
        #     correct += 1
        # elif not line[3] == line[4]

corr = true_of_false.count(True)
incor = true_of_false.count(False)

print('all:{}\ncorr:{}\nincorr:{}\nnone:{}'.format(len(true_of_false), corr, incor, none_cnt))
