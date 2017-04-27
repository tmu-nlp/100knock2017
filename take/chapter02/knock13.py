import subprocess

with open('col1.txt') as col1, open('col2.txt') as col2, open('col1col2.txt', 'w') as m:
    for c1, c2 in zip(col1.readlines(), col2.readlines()):
        m.write(c1.rstrip('\n') + '\t' + c2)

print(" --- check; paste cmd --- ")
cmd = 'paste -d "\t" col1.txt col2.txt'
subprocess.call(cmd, shell=True)