if __name__ == '__main__':
    with open('data/questions-words.txt') as i_f,open('data/answer91.txt','w') as o_f:
        for line in i_f:
            tokens = line.split()
            if tokens[0] == ':':
                if tokens[1] == 'family':
                    flag = 1
                    continue
                else:
                    flag = 0
                    continue
            if flag == 1:
                o_f.write(line)
