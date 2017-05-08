import subprocess

col1list = []
with open('hightemp.txt') as f:
    for l in f.readlines():
        c = l.split('\t')
        col1list.append(c[0])
print(len(set(col1list)))

print(" --- check; sort and uniq --- ")
cmd = "awk '{ print $1 }' hightemp.txt | sort | uniq | wc -l | tr -d \" \""
subprocess.call(cmd, shell=True)