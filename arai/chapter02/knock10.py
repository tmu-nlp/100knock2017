f=open('hightemp.txt', "r")
count = 0
for line in f:
    print(line)
    count+=1
print(count)
    
f.close()

