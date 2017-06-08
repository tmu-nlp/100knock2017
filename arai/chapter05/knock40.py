class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def printmorph(self):
        return [self.surface, self.base, self.pos, self.pos1]

def cabocha_data():    
    with open('neko.txt.cabocha') as text:
        mlist = []
        Mlist = []
        for line in text:
            word = line.strip('\n').replace('\t',',').split(',')
            if word[0] == 'EOS':
                if len(mlist) > 0:
                    Mlist.append(mlist)
                    mlist = []
            elif word[0].startswith('*'):
                continue
                
            else:
                mkeys = Morph(word[0], word[7], word[1], word[2])
                mlist.append(mkeys)
    return Mlist

if __name__ == '__main__':
    for i,line in enumerate(cabocha_data()):
        if i == 3:
            for word in line:
                print(word.printmorph())
            break

