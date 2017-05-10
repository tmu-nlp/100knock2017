f = open('hightemp.txt')

lines = []

for i in f:
    i = i.split()
    lines.append(i)
sorted(lines, key=lambda temp: temp[2])
#list.sort()はリストしかできないけど
#sorted()はそれ以外もできる
lines.reverse()

for l in lines:
    print(l)

f.close()
