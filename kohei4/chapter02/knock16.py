# coding: utf-8
import sys
n = int(sys.argv[1])

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

ln = len(lines)

for i in range(ln//n + 1):
    with open('hightemp_' + str(i) + '.txt', 'w') as f :
        f.write(''.join(lines[i*n:(i+1)*n]))
#        print(''.join(lines[i*n:(i+1)*n]))
## split -l 3 hightemp.txt
