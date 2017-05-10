f = open('hightemp.txt','r')
counter = 0
for l in f:
    counter += 1
print(counter)
f.close()
