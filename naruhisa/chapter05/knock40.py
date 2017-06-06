class Morph:
    def _init_(self, surface, base, pos, pos1):
        self.surface = ''
        self.base = ''
        self.pos = ''
        self.pos1 = ''
'''
    def Get_surface():
        return surface
    def Get_base():
        return base
    def Get_pos():
        return pos
    def Get_pos1():
        return pos1
'''

def func1():
    with open('neko.txt.cabocha', 'r') as f:
        tmp = list()
        for line in f:
            line = line.replace(' ', ',')
            words = (line.replace('\t', ',')).strip().split(',')
            kts = Morph()
            if(words[0] != '*' and words[0] != 'EOS'):
                kts.surface = words[0]
                kts.base = words[7]
                kts.pos = words[1]
                kts.pos1 = words[2]
                tmp.append(kts)
            elif(words[0] == 'EOS'):
                yield tmp
                tmp = list()


if __name__ == '__main__':
    for i, x in enumerate(func1()):
        if i == 2:
            for line in x:
                print(line.surface, end=' ')
                print(line.base, end=' ')
                print(line.pos, end=' ')
                print(line.pos1)
            break
