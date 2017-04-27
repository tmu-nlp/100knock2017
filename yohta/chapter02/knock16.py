f = open('hightemp.txt','r')
n = int(input("分割行数:"))
counter = 0
for l in f:
#    counter += 1
    if (counter < n):
#        counter += 1
        print(l)
    else:
#        counter = 0
        print()
        print()
        print(l)
        counter = 1
        continue
    counter += 1
