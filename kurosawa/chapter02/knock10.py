f = open('hightemp.txt', 'r')
n = 0
for line in f:
    n += 1
print(n)
f.close()

# wc -l hightemp.txt
