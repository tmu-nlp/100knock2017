f=open('hightemp.txt', "r")
f1=open('col1.txt', "w")
f2=open('col2.txt', "w")
for line in f:
    line2=line.split()
    f1.write(line2[0] + '\n')
    f2.write(line2[1] + '\n')

