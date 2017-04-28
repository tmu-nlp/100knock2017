# coding: utf-8
import sys
import os

with open('hightemp.txt', 'r') as f:
    col1=[]

    for line in f:
        ftab=line.index("\t")
        col1.append("".join(line[:(ftab)]))

# col1_text="\n".join(col1)

set_col1 = set(col1)

print(sorted(set_col1))

## Shell command
print()
os.system("cut -f1  hightemp.txt | sort  | uniq")
