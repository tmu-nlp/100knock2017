import re

class Morph:
    def __init__(self, word):
        self.surface = word[0]
        self.base = word[-3]
        self.pos = word[1]
        self.pos1 = word[2]

def cabocha_morph_data(data):
    pettern = re.compile(r'\* ')
    morph_sentence = []
    for line in data:
        if pettern.match(line):
            continue
        elif line == 'EOS\n':
            if morph_sentence != []:
                yield morph_sentence
                morph_sentence = []
            continue
        else:
            word = line.replace('\t', ',').split(',')
            morph_sentence.append(Morph(word))

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        for i, line in enumerate(cabocha_morph_data(data_in)):
            if i+1 == 3:
                for word in line:
                    print('\t'.join([word.surface, word.base, word.pos, word.pos1]))
                break
