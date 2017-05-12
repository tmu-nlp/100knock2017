import collections

def mecab_dict_line(line):
    words = line.replace('\t', ' ').replace(',', ' ').split()
    mecab_word = {'surface' : words[0], 'base' : words[-3], 'pos' : words[1], 'pos1' : words[2]}
    return mecab_word

def mecab_dict_data(data):
    mecab_sentence = []
    mecab_data = []
    for line in data:
        if line == 'EOS\n':
            if mecab_sentence != []:
                mecab_data.append(mecab_sentence)
                mecab_sentence = []
        else:
            mecab_sentence.append(mecab_dict_line(line))
    return mecab_data

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = mecab_dict_data(data_in)
    with open('../data/neko_line.txt', 'w') as data_out:
        for line in mecab_data:
            data_out.write(str(line) + '\n')
