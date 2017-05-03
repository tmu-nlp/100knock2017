f = open('hightemp.txt')
N = int(input())

count = 0
for line in f:
    if count < N:
        print(line)
        count += 1
    else:
        break

f.close()
