f = open('hightemp.txt','r')
n = int(input('number:'))
counter = 1
for l in f:
    if counter <= n:
        print(l)
    counter += 1
