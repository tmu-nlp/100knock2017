import subprocess

with open('col1.txt','w') as col1, open('col2.txt', 'w') as col2:
    with open('hightemp.txt') as f:
        for l in f.readlines():
            splitline = l.split('\t')
            col1.write(splitline[0] + '\n')
            col2.write(splitline[1] + '\n')

print(" --- check; cut cmd for col1 --- ")
cmd = "cat hightemp.txt | cut -f1"
subprocess.call(cmd, shell=True)

print("\n --- check; cut cmd for col2 --- ")
cmd = "cat hightemp.txt | cut -f2"
subprocess.call(cmd, shell=True)