f = open('hightemp.txt','r')
f1 = open('col1.txt','w')
f2 = open('col2.txt','w')
for l in f:
    cols = l.split('\t')
    f1.writelines(cols[0])
    f1.write('\n')
    f2.writelines(cols[1])
    f2.write('\n')
#print(cols)
#print(cols[0])
#print(cols[1])
