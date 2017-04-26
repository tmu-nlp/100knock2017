# coding: utf-8
import sys

nl = ''
with open('col1.txt', 'r') as f1, open('col2.txt','r') as f2 :
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if not (line1 + line2):
            break

        nl = nl + line1.strip('\n') + "\t" + line2

with open('merged.txt', 'w') as f:
    f.write(nl)
