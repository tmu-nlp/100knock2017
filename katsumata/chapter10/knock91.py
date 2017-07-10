
if __name__ == '__main__':
    input_file = 'questions-words.txt'
    flag_fam = False
    with open(input_file) as i_f,open('analogy.family', 'w') as o_f:
        for line in i_f:
            if flag_fam:
                if line[0] == ':':
                    break
                o_f.write(line)

            if line.strip() == ': family':
                flag_fam = True
