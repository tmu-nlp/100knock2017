def get_morphs(file_name):
    sentence = list()
    for line in open(file_name):
        if line.startswith('EOS'):
            if len(sentence) > 0:
                yield sentence
            sentence = list()
        else:
            mecab_line = line.rstrip('\n').split('\t')
            morph = mecab_line[-1].split(',')
            word = {'surface': mecab_line[0], 'base': morph[6], 'pos': morph[0], 'pos1': morph[1]}
            sentence.append(word)

if __name__ == '__main__':
    for sentence in get_morphs('./neko.txt.mecab'):
        for word in sentence:
            print(word)
