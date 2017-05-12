text1 = open('col1.txt', 'r')
text2 = open('col2.txt', 'r')
ntext = open('col3.txt', 'w')

tmpw = ''
tmp = []
i = 0
for line1 in text1:
    for j in range(len(line1)):
        if(line1[j] == '\n'):
            break
        else:
            tmpw += line1[j]
    tmp.append(tmpw)
    tmpw = ''

for line2 in text2:
    ntext.write(tmp[i] + '\t' + line2)
    i += 1


text1.close()
text2.close()
ntext.close()
