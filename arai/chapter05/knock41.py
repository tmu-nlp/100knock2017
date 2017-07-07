from knock40 import Morph
from collections import defaultdict

class Chunk:
    def __init__(self, dst, srcs):
        self.morphs = list()
        self.dst = dst
        self.srcs = srcs
    def printchunk(self):
        return [self.morphs, self.dst, self.srcs]
    
    def printsurface(self):
        surface_list = []
        for w in self.morphs:
            surface_list.append(w.surface)
        return surface_list 
    
    def printsurface42(self):
        surface_list42 = []
        surface_list = []
        for w in self.morphs:
            surface_list.append(w.surface)
            surface_list42.append(w.surface_list[0])
        return surface_list42

    def get_word_only_morphs(self):
        return [morph for morph in self.morphs if morph.pos != '記号']

    def get_word_only(self):
        return ''.join([morph.surface for morph in self.get_word_only_morphs()])

    def get_morphs(self):
        return self.morphs

def cabocha_data():    
    with open('neko.txt.cabocha') as text:
        mlist = []
        Mlist = []
        src_dict = defaultdict(list)
        for line in text:
            word = line.strip('\n').replace('\t',',').split(',')
            if word[0].startswith('*'):
                word = word[0].split()
                dst = int(word[2].strip('D'))
                chunk = Chunk(dst, src_dict[int(word[1])])
                src_dict[dst].append(int(word[1]))
                mlist.append(chunk)
            elif word[0] == 'EOS':
                src_dict = defaultdict(list)
                if len(mlist) > 0:
                    Mlist.append(mlist)
                    mlist = []
            else:
                morphs = Morph(word[0], word[7], word[1], word[2])
                chunk.morphs.append(morphs)

    return Mlist

if __name__ == '__main__':
    for i,line in enumerate(cabocha_data()):
        if i == 8:
            for word in line:
                print(word.printsurface(),  word.dst)
            break
