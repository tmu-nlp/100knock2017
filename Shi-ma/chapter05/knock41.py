from knock40 import Morph
import re
import collections

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    def get_word_chunk(self):
        return [s.surface for s in self.morphs]
    def get_phrase_txt(self):
        phrase_txt = ''
        for morph in self.morphs:
            if morph.pos == '記号':
                continue
            else:
                phrase_txt += morph.surface
        return phrase_txt
    def get_phrase_list(self):
        phrase_list = []
        for morph in self.morphs:
            if morph.pos == '記号':
                continue
            else:
                phrase_list.append(morph.base)
        return phrase_list
    def get_phrase_pos(self):
        phrase_pos = []
        for morph in self.morphs:
            if morph.pos == '記号':
                continue
            else:
                phrase_pos.append(morph.pos)
        return phrase_pos
    def get_phrase_pos1(self):
        phrase_pos1 = []
        for morph in self.morphs:
            if morph.pos == '記号':
                continue
            else:
                phrase_pos1.append(morph.pos1)
        return phrase_pos1
    def get_phrase_XY(self, XY):
        phrase_XY = ''
        flag = 0
        for morph in self.morphs:
            if morph.pos == '記号':
                continue
            elif flag == 0 and morph.pos == '名詞':
                phrase_XY += XY
                flag = 1
            else:
                phrase_XY += morph.surface
        return phrase_XY

def cabocha_chunk_data(data):
    pettern = re.compile(r'\* ')
    chunk_sentence = [];
    morphs = []; srcs = collections.defaultdict(lambda: [])
    for line in data:
        if pettern.match(line):
            if morphs != []:
                chunk_sentence.append(Chunk(morphs, dst, srcs[num_chunk]))
                morphs = [];
            temp = line.split()
            num_chunk = int(temp[1])
            dst = int(re.match(r'-*[0-9]+(?=D)', temp[2]).group())
            if dst != -1:
                srcs[dst].append(num_chunk)
        elif line == 'EOS\n':
            if chunk_sentence != [] or morphs != []:
                chunk_sentence.append(Chunk(morphs, dst, srcs[num_chunk]))
                yield chunk_sentence
                chunk_sentence = []
                morphs = []; srcs = collections.defaultdict(lambda: [])
        else:
            word = line.replace('\t', ',').split(',')
            morphs.append(Morph(word))

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        num_line = 8
        for i, line in enumerate(cabocha_chunk_data(data_in)):
            if i+1 == num_line:
                for word in line:
                    word_chunk = word.get_word_chunk()
                    print('{}\t{}\t{}'.format(word_chunk, [word.dst], word.srcs))
                break
