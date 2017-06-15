class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.getSurface(),self.getBase(),self.getPos(),self.getPos1())

    def getSurface(self):
        return self.surface
    def getBase(self):
        return self.base
    def getPos(self):
        return self.pos
    def getPos1(self):
        return self.pos1

    def getMlist(self):
        mlist = list()
        mlist.append(self.surface)
        mlist.append(self.base)
        mlist.append(self.pos)
        mlist.append(self.pos1)
        return mlist
#    def setSurface():

"""
    def output(self):
#        print('surface\tbase\tpos\tpos1')
        print('{}\t{}\t{}\t{}'.format(self.surface,self.base,self.pos,self.pos1))
"""

def func40(i):
    with open('../data/neko.txt.cabocha','r') as neko:
        sentence_counter = 1
#          sentence = []
#      a = Morph(surface,base,pos,pos1)
        print('surface\tbase\tpos\tpos1')
        for line in neko:
#                              sentence = []
            line = line.replace(',',' ')
            line = line.replace('\t',' ')
            line = line.replace('\n',' ')
            element = line.split()
            if not element[0] == '*' and not element[0] == 'EOS' and not element[1] == '空白':
                sentence = list()
#                print(element[7])
#                a.getSurface(element[0])
#                a.getBase(element[7])
#                a.getPos(element[1])
#                a.getPos1(element[2])
                a = Morph(element[0],element[7],element[1],element[2])
#                sentence.append(a)
#                yield sentence
                if sentence_counter == i:
#                    a.output()
#                if sentence_counter == i:
                    print('{}\t{}\t{}\t{}'.format(a.getSurface(),a.getBase(),a.getPos(),a.getPos1()))
            if element[0] == 'EOS':
                sentence_counter += 1

if __name__ == '__main__':
    func40(3)
"""
    with open('../data/neko.txt.cabocha','r') as neko:
        count = 1
        for num,line in enumerate(func40()):
            if line == 'EOS':
                count += 1
            while(count < 3):
                print(line)
"""
