import sys
from Class import Morph

def make_morph():
    with open(sys.argv[1]) as read_file:
        sentence = list()
        for line in read_file:
            if line.startswith('EOS'):
                yield sentence
                sentence = list()
            elif line.startswith('*'):
                continue
            else:
                line = line.split('\t')
                line[1] = line[1].split(',')
                sentence.append(Morph(line[0],line[1]))

if __name__ == '__main__':
    for i, line_main in enumerate(make_morph()):
        if i == 2:
            for j in range(len(line_main)):
                print(line_main[j].get_morph())
            break
