data = []
for line in open('hightemp.txt'):
    data.append(line.split())

for line2 in sorted(data, key=lambda x: x[2]):
    print(line2)
 

