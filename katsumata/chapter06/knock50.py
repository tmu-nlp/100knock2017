def split_sentence():
    nlp_file = 'nlp.txt'
    true_line = ''
    fin_symbol = ['.',';',':','?','!']
    with open(nlp_file, 'r') as i_f:
        for pre_line in i_f:
            for i, words in enumerate(pre_line):
                true_line += words
                if not words in fin_symbol:
                    continue
                if pre_line[i+1] == ' ' and 'A' <= pre_line[i+2] <= 'Z':
                    yield (true_line.lstrip(' '))
                    true_line = ''
        yield(true_line.lstrip(' '))            
if __name__ == '__main__':
    for line in split_sentence():
        print (line)
