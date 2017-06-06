from Chunk import Chunk
from Morph import Morph 
from collections import defaultdict
def make_chunk_list():
    chunk_list = list()
    temp_list = list()
    phrase_list = list()
    temp_dict = defaultdict(list)
    with open('neko.txt.cabocha', 'r') as neko:
        for line in neko:
            if line.split(' ')[0] == '*': #係り受けの処理
                if line.split(' ')[1] != '0': #次の係り受け記述を見つけたらそれまでのものを追加
                    chunk = Chunk(phrase_list, chunks[2], temp_dict[chunks[1]])
                    phrase_list = list()
                    temp_list.append(chunk)
                chunks = line.split(' ')
                chunks[2] = chunks[2].replace('D', '')
                temp_dict[chunks[2]].append(chunks[1])
            elif line.strip() == 'EOS': #リストを取りまとめる
                chunk = Chunk(phrase_list, chunks[2], temp_dict[chunks[1]])
                phrase_list = list()
                temp_list.append(chunk)
                chunks = ['0'] * 3
                temp_dict = defaultdict(list)
                chunk_list.append(temp_list)
                temp_list = list()
            else:   #形態素の処理
                line = line.replace('\t', ',')
                words = line.strip().split(',')
                morph = Morph(words[0], words[7], words[1], words[2])
                phrase_list.append(morph)
    return chunk_list

if __name__ == '__main__':
    chunk_list = make_chunk_list()
    for elements in chunk_list[7]:
        morphs = elements.getMorphs()
        dst = elements.getDst()
        #srcs = elements.getSrcs()
        for morph in morphs:
            print ('{}'.format(morph.getSurface()), end='')
        print (' {}'.format(dst))
