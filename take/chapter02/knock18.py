import subprocess

with open('hightemp.txt') as f:
    l = f.readlines()

lot = []
for s in l:
    lot.append(tuple(s.split('\t')))

for x in sorted(lot, key=lambda x:x[2], reverse=True):
    print(x)

print(" --- check; sort --- ")
cmd = "cat hightemp.txt | sort -rnk 3,3"
subprocess.call(cmd, shell=True)