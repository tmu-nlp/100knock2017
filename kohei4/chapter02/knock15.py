# coding: utf-8
import sys
n = int(sys.argv[1])

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

ln = len(lines)

print(''.join(lines[ln-n:ln]),end='')
