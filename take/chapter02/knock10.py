import subprocess

print(sum(1 for l in open('hightemp.txt')))

print(" --- check; wc cmd --- ")
cmd = 'cat hightemp.txt | wc -l | tr -d " " '
subprocess.call(cmd, shell=True)