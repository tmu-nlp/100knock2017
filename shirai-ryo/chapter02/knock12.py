with open('hightemp.txt') as f:
#一行目
    f_1 = open('col1.txt', 'w')
#二行目
    f_2 = open('col2.txt', 'w')
    for line in f:
        lines = line.split()
        f_1.write(lines[0] + '\n')
        f_2.write(lines[1] + '\n')

f_1.close()
f_2.close()
