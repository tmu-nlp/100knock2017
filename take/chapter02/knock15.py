import sys
import subprocess

arg = sys.argv
if len(arg) < 2:
    print('plz specify line number.')
    sys.exit(2)

try:
    N = int(arg[1])
except ValueError:
    print("Could not convert to integer.")
    exit(1)

with open('hightemp.txt') as f:
    lines = f.readlines()
    for line in lines[-N:-1]:
        print(line, end='')
    print(lines[-1], end='')

print(" --- check; tail cmd --- ")
cmd = 'cat hightemp.txt | tail -{}'.format(N)
subprocess.call(cmd, shell=True)