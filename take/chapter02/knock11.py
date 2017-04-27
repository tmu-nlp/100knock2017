import subprocess

with open('replaced.txt', 'w') as rf, open('hightemp.txt', 'r') as f:
    for l in f.readlines():
        rf.write(l.replace('\t', ' '))

print(" --- check; sed(BSD) cmd--- ")
cmd = "sed s/$'\\t'/' '/g hightemp.txt"
subprocess.call(cmd, shell=True)