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
    for line in f.readlines()[0:N]:
        print(line, end='')

print(" --- check; head cmd --- ")
cmd = 'cat hightemp.txt | head -{}'.format(N)
subprocess.call(cmd, shell=True)