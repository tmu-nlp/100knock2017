# coding: utf-8
import sys
f = open('hightemp.txt', 'r')
text = str(f.read())

cnt = 0
for i in range(len(text)):
    if text[i] == '\n':
        cnt = cnt + 1

print(cnt)
