f = open('hightemp.txt','r')
n = int(input('N > '))
i = 0
for line in f:
    i += 1
j = 0
f.close()
f = open('hightemp.txt','r')
for line in f:
    if j>=i-n:
        print(line.replace('\n',''))
    j += 1
f.close()

# tail -2 hightemp.txt
