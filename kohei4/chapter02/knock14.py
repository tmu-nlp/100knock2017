# coding: utf-8
import sys
n = int(sys.argv[1])

with open('hightemp.txt', 'r') as f:
    for i in range(n):
        print(f.readline(),end="")

# shell head -n 3 hightemp.txt        
