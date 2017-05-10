input_n = int(input())

text = open('hightemp.txt', 'r')

count = 0

tmp = []
for line in text:
    count += 1
    tmp.append(line)

for i in range(count):
    if(count - input_n < i + 1):
        print(tmp[i])

text.close()
