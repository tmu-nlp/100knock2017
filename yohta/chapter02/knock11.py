f1 = open('hightemp.txt','r')
result = []
for l in f1:
    l = l.replace('\t',' ')
    print(l)
    result += l
#print(l)
#f1.close()
f2 = open('hightemp_after.txt','w')
f2.writelines(result)
#print (type(result))
#f2.close()
