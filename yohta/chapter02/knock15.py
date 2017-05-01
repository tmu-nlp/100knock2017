f1 = open('hightemp.txt','r')
n = int(input('number:'))
counter = 0
linef = 0
for i in f1:
    linef += 1
#print('line:',int(linef))

f2 = open('hightemp.txt','r')
for l in f2:
#    print(l)
#    counter += 1
    if (counter - linef + n >= 0):
        print(l)
    counter += 1
