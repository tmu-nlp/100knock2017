if __name__ == '__main__':
    with open('questions-words.txt', 'r') as i_f, open('ccc.txt', 'w') as o_f:
        flag = 0
        for line in i_f:
            if flag == 0 and line.strip() == ': family':
                flag = 1
            elif flag == 1 and line[0] == ':':
                flag = 0
            elif flag == 1:
                o_f.write(line)
