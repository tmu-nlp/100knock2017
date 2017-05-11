text = open('hightemp.txt', 'r')

tmp = []
for line in text:
    tmp.append(line)

tmp = sorted((tmp), key=lambda temp:temp[2])
for i in range(len(tmp)):
    print(tmp[len(tmp) - 1 - i])
text.close()
