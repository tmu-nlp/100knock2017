'''
Usage
$ python knock50.py| python knock51.py
'''

import sys

lines_list = sys.stdin.readlines()

for line in lines_list:
    wordlist = line.split(' ')
    for w in wordlist:
        print(w)
