import math
#分割数
split_n = int(input('n行分割: '))

#1要素1行のリスト
list_rows = []

with open('hightemp.txt', 'r') as f_input:
    num_row = 0 #総行数_24
    for row in f_input:
        list_rows.append(row)
        num_row += 1
    #割り切れなかった時のpop水増し
    if num_row%split_n != 0:
        for k in range(split_n-(num_row%split_n)):
            list_rows.append('')

    #作成するファイル数
    num_separate = math.ceil(num_row / split_n)
    print ('作成したファイル数:', end='')
    print (num_separate)
    
    for i in range(int(num_separate)):
        with open('hightemp_'+str(i)+'.txt', 'w') as f_output:
            for j in range(split_n):
                f_output.writelines(list_rows.pop(0))
#split -l 5 hightemp.txt test_
