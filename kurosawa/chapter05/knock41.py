import sys
from collections import defaultdict
from Class import Morph, Chank

def make_chank():
    with open(sys.argv[1]) as read_file:
        sentence = list()
        src = defaultdict(list)
        for line in read_file:
            if line.startswith('EOS'):
                sentence.append(chank)
                yield sentence
                sentence = list()
                src = defaultdict(list)
            elif line.startswith('*'):
                line = line.split()
                if line[1] != '0':
                    sentence.append(chank)
                dst = line[2].strip('D')
                src[dst].append(line[1])
                chank = Chank(dst,src[line[1]])
            else:
                line = line.split('\t')
                line[1] = line[1].split(',')
                chank.set_morphs(Morph(line[0],line[1]))


if __name__ == '__main__':
    for i, line_main in enumerate(make_chank()):
        if i == 7:
            for j in range(len(line_main)):
                str1 = ''
                for morph_print in line_main[j].get_morphs():
                    str1 += morph_print.get_surface()
                print('{}→{}'.format(str1,line_main[j].get_dst()))
