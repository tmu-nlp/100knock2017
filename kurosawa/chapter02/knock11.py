f = open('hightemp.txt','r')
f1 = open('hightemp1.txt','w')
for line in f:
    f1.write(line.expandtabs(1))
f.close()
f1.close()
