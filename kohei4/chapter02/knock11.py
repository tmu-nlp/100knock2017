# coding: utf-8
import sys
import os

with open('hightemp.txt', 'r') as f:
    tex_list = list(str(f.read()))

n_text = []
for i in range(len(tex_list)):
    if tex_list[i] == '\t':
        tex_list[i] = ' '

n_text = ''.join(tex_list)

with open('new_hightemp.txt','w') as f2:
    f2.write(n_text)


os.system("tr '\t' ' ' < ./hightemp.txt")
