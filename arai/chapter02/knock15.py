import sys
n=int(sys.argv[1])
f=open('hightemp.txt', "r")
lines=[]
for line in f:
    lines.append(line)
for i in range(len(lines)-(n),len(lines)):
    print(lines[i])


