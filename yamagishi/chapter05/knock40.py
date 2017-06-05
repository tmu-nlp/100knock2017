class Morph:
    def __init__(self, surface, pos, pos1, base):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def get_morph(self):
        return {'surface':self.surface, 'base':self.base, 'pos':self.pos, 'pos1':self.pos1}

    def get_surface(self):
        return self.surface

    def get_base(self):
        return self.base

    def get_pos(self):
        return self.pos

    def get_pos1(self):
        return self.pos1


def get_morph_list():
    sentence = list()
    for line in open('./neko.txt.cabocha'):
        if line.startswith('*'):
            continue
        elif line.startswith('EOS'):
            if len(sentence) > 0:
                yield sentence
            sentence = list()
        else:
            surface, morphs = line.rstrip('\n').split('\t')
            morphs = morphs.split(',')
            sentence.append(Morph(surface, morphs[0], morphs[1], morphs[6]))

if __name__ == '__main__':
    for i, sentence in enumerate(get_morph_list()):
        if i == 5:
            for morph in sentence:
                print(morph.get_morph())
            break
