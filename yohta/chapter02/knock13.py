f1 = open('col1.txt','r')
f2 = open('col2.txt','r')
f = open('cols.txt','w')
for i,j in zip(f1,f2):
    i = i.strip('\n')
    f.writelines(i + '\t' + j)
#    f.write('\n')
