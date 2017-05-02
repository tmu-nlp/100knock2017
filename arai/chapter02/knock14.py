import sys

f=open('hightemp.txt' , "r")
count=0
for line in f:
    count+=1
    print(line)
    if count == int(sys.argv[1]):
        break
