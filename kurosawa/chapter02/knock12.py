f = open('hightemp.txt','r')
f1 = open('col1.txt','w')
f2 = open('col2.txt','w')
for line in f:
    line = line.split()
    f1.write(line[0] + '\n')
    f2.write(line[1] + '\n')
f.close()
f1.close()
f2.close()
