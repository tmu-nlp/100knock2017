from collections import Counter
import subprocess

with open('col1.txt') as f:
    counter = Counter(f.readlines())
    # print(counter)
    for val, cnt in counter.most_common():
        print('{0}回: {1}'.format(cnt,val), end='')

print(" --- check; cut, uniq and sort --- ")
cmd = 'cat hightemp.txt  | cut -f1 | sort -k1,1 | uniq -c | sort -rk1,1'
subprocess.call(cmd, shell=True)