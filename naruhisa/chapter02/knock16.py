input_n = input('input:')
count = 0
ex_count = 0
word = open('hightemp.txt', 'r')
tmp = []
i = 0
for line in word:
    tmp.append(line)
    count += 1
text = []
while(i < count):
    ex_count += 1
    with open('text{}.txt'.format(ex_count), 'w') as text:
        for _ in range(int(input_n)):
            text.write(tmp[i])
            i += 1

word.close()
