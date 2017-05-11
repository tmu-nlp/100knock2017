f = open('hightemp.txt')
data = []
for line in f:
    line2 = line.strip().split()
    if line2[0] not in  data:
        data.append(line2[0])
print(data)    





