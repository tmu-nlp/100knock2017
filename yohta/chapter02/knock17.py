f = open('hightemp.txt','r')
cols = ""
for l in f:
    col = l.split('\t')
    if not(col[0] in cols):
        cols += col[0]
        cols += '\n'
print(cols)
