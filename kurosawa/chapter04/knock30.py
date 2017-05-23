import sys

def make_map(get_morpheme):
    neko_map = {}
    get_morpheme = get_morpheme.replace(',','\t').split('\t')
#    print(get_morpheme)
    neko_map['surface'] = get_morpheme[0]
    neko_map['base'] = get_morpheme[7]
    neko_map['pos'] = get_morpheme[1]
    neko_map['pos1'] = get_morpheme[2]
#    print(neko_map)
    return neko_map

def make_list(file_name):
    with open(file_name) as read_file:
        neko_list = []
        neko_sentence = []
        for line in read_file:
            line = line.strip()
            if line != 'EOS':
                neko_sentence.append(make_map(line))
#                print(neko_sentence)
            else:
                neko_list.append(neko_sentence)
                neko_sentence = []
    return neko_list

if __name__ == '__main__':
    print(make_list(sys.argv[1]))
