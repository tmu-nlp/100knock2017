f1 = open('col1.txt', 'r')
f2 = open('col2.txt', 'r')
f = open('merge.txt', 'w')

for line1,line2 in zip(f1,f2):
    f.write(line1.replace('\n','') + '\t' + line2)
f1.close()
f2.close()
f.close()
