# coding: utf-8
import sys
import os

with open('hightemp.txt', 'r') as f:
    table = f.readlines()

table.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)
#table.sort(key=lambda line: float(line.split('\t')[2]))




print(*table)

## Shell command
print()
os.system("sort -k3 -n -r hightemp.txt")
