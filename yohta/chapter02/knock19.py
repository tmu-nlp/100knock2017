from collections import defaultdict
import sys
f = open('hightemp.txt','r')

cols = ""
counts = defaultdict(lambda: 0)
cols_s = []
for l in f:
    col = l.split('\t')
#    print(col)
    cols += col[0]
    cols += '\n'
for w in cols:
    cols_l = cols.split('\n')
for n in range(len(cols_l)):
    if len(cols_l[n]) > 0:
        cols_s.append(cols_l[n])

for word in cols_s:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word,n in sorted(counts.items(),key = lambda x:x[1],reverse = True):
    print(word + " " + str(counts[word]))
#print(type(cols_l))
#print(type(counts))

#for word in cols_l:
#        cols_counter[word] += 1
#    else:
#        cols_counter[word] = 1
#print (cols_counter)

#print (cols_l[0])
#print (type(cols_counter))
#for word in cols_l:
#    if (word in cols_l):
#        cols_counter[word] += 1
#    else:
#        cols_counter[word] = 1
#    print (type(w))
