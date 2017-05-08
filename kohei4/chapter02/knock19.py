# coding: utf-8
import sys
import os
from collections import Counter

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()
    col1 = []
for line in lines:
    col1.append(line.split('\t')[0])

col1_counter = Counter(col1)

for pref, cnt in col1_counter.most_common():
    print(cnt, pref)

## Shell command
print()
os.system("cut -f1 hightemp.txt | sort | uniq -c | sort -n -k1 -r" )
