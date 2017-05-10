f=open('hightemp.txt', "r")
for line in f:
    line2=line.replace("\t", "  ")
    print(line2)
f.close()
