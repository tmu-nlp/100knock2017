from Morph import Morph

def make_morph_list():
    morph_list = list()

    keys = ['surface', 'base', 'pos', 'pos1']
    indexes = [0,7,1,2]
    """
    index
    0:表層形
    1:品詞
    2:品詞細分類1
    7:原形
    """
    temp_list = list()
    with open('neko.txt.cabocha', 'r') as neko:
        for line in neko:
            if line.split(' ')[0] == '*':
                continue
            temp_dict = dict()
            line = line.replace('\t', ',')
            #line = line.replace(',', ' ')
            #print (line)
            words = line.strip().split(',')
            if words[0] != 'EOS':
                a = Morph(words[0],words[7],words[1],words[2])
                temp_list.append(a)
            else:
                #if len(temp_list) != 0:
                morph_list.append(temp_list)
                temp_list = list()
    return morph_list

if __name__ == '__main__':
    morph_list = make_morph_list()
    print('表層形 原形 品詞 品詞細分類')
    for elements in morph_list[2]:
        surface = elements.getSurface()
        base = elements.getBase()
        pos = elements.getPos()
        pos1 = elements.getPos1()
        print('{} {} {} {}'.format(surface, base, pos, pos1))
    #print (morph_list[3])
