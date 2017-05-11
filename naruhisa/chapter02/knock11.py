word = open('hightemp.txt', 'r')

for line in word:
    line = line.strip()
    for i in range(len(line)):
        if(line[i] == '\t'):
            print(' ', end='')
        else:
            print(line[i], end='')
    print()
word.close()
