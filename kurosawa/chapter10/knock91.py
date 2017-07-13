

if __name__ == '__main__':
    with open('questions-words.txt') as data, open('family.txt','w') as family:
        for line in data:
            line_s = line.split()
            if line_s[0] == ':':
                if line_s[1] == 'family':
                    flag = 1
                    continue
                else:
                    flag = 0
                    continue
            if flag == 1:
                family.write(line)

