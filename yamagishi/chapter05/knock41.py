from knock40 import Morph
from collections import defaultdict


class Chunk:
    def __init__(self, dst, srcs):
        self.morphs = list()
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return 'dst: {}, srcs: {}, string: {}'.format(self.dst, self.srcs, self.get_string())

    def get_string(self):
        return ' '.join([morph.get_surface() for morph in self.morphs])

    def get_word_only(self):
        return ''.join([morph.get_surface() for morph in self.get_word_only_morphs()])

    def get_morphs(self):
        return self.morphs

    def get_word_only_morphs(self):
        return [morph for morph in self.morphs if morph.get_pos() != '記号']

    def get_change_char(self, char):
        ans = list()
        flag = False
        for morph in self.get_word_only_morphs():
            if flag is False and morph.get_pos() == '名詞':
                ans.append(char)
                flag = True
            else:
                ans.append(morph.get_surface())
        return ''.join(ans)
    
    def get_dst(self):
        return self.dst

    def get_srcs(self):
        return self.srcs

    def has_noun(self):
        return any(morph.get_pos() == '名詞' for morph in self.morphs)

    def append_morph(self, morph):
        self.morphs.append(morph)


def get_neko_list(n=float('inf')):
    neko_list = list()
    sentence = list()
    src = defaultdict(list)
    for line in open('./neko.txt.cabocha'):
        if len(neko_list) > n:
            break

        if line.startswith('*'):
            ids = line.rstrip('\n').split()
            chunk_id = int(ids[1])
            dst = int(ids[2].rstrip('D'))
            src[dst].append(chunk_id)
            chunk = Chunk(dst, src[chunk_id])
            sentence.append(chunk)

        elif line.startswith('EOS'):
            if len(sentence) > 0:
                neko_list.append(sentence)
            sentence = list()
            src = defaultdict(list)

        else:
            surface, morphs = line.rstrip('\n').split('\t')
            morphs = morphs.split(',')
            morph = Morph(surface, morphs[0], morphs[1], morphs[6])
            chunk.append_morph(morph)

    return neko_list

if __name__ == '__main__':
    neko_list = get_neko_list(8)
    sentence = list()
    for chunk in neko_list[7]:
        print(chunk)
        sentence.append(chunk.get_string())
    print(' '.join(sentence))
