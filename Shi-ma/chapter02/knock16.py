import sys
import math

N = int(sys.argv[1])
n = 1
with open('../data/hightemp.txt', 'r') as data:
    for line in data:
        print(line, end='')
        if n%N == 0:
            print('')
        n += 1
