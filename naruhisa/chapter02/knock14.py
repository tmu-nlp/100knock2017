input_n = int(input())

text = open('hightemp.txt', 'r')

count = 0
for line in text:
    if count > input_n - 1:
        break
    count += 1
    print(line)

text.close()
