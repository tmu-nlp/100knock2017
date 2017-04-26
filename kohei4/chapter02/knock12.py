# coding: utf-8
import sys


with open('hightemp.txt', 'r') as f:
    col1=[]
    col2=[]
    for line in f:
        ftab=line.index("\t")
        col1.append("".join(line[:(ftab)]))
        dtab=line.index("\t",ftab+1)
        col2.append("".join(line[ftab+1:dtab]))

col1_text="\n".join(col1)
col2_text="\n".join(col2)

with open('col1.txt','w') as c1:
    c1.write(col1_text)

with open('col2.txt','w') as c2:
    c2.write(col2_text)
