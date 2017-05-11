f = open('hightemp.txt','r')
n = int(input('N > '))
i = 0
for line in f:
    print(line.replace('\n',''))
    i += 1
    if i==n:
        break
f.close()

# head -2 hightemp.txt
