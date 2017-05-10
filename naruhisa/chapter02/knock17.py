text = open('hightemp.txt', 'r')

count = 0

tmp = set()
for line in text:
    for i in range(len(line)):
        if line[i] == ' ' or line[i] == '\t':
            tmp.add(line[0:i])
            break

print(tmp)
text.close()
