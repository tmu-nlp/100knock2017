# coding: utf-8
import sys
with open('hightemp.txt', 'r') as f:
    text = str(f.read())

cnt = 0
for i in range(len(text)):
    if text[i] == '\n':
        cnt = cnt + 1

print(cnt)
