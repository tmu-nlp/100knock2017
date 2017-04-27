f = open('hightemp.txt','r')
cols = []
for l in f:

    col = l.split('\t')
#    cols += col
#    col.strip('\n')
    cols.append(col)
for i in sorted(cols, key = lambda x: x[2]):
    print('{0}\t{1}\t{2}\t{3}'.format(i[0],i[1],i[2],i[3]),end = '')
