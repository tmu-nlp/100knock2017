from knock40 import Morph
from collections import defaultdict


class Chunk:
    def __init__(self, dst, srcs):
        self.morphs = list()
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return 'dst: {}, string: {}'.format(self.dst, self.get_string())

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

    def has_verb(self):
        return any(morph.get_pos() == '動詞' for morph in self.morphs)

    def append_morph(self, morph):
        self.morphs.append(morph)


def get_neko_list():
    sentence = list()
    src = defaultdict(list)
    for line in open('./neko.txt.cabocha'):
        if line.startswith('*'):
            ids = line.rstrip('\n').split()
            chunk_id = int(ids[1])
            dst = int(ids[2].rstrip('D'))
            src[dst].append(chunk_id)
            chunk = Chunk(dst, src[chunk_id])
            sentence.append(chunk)

        elif line.startswith('EOS'):
            if len(sentence) > 0:
                yield sentence
            sentence = list()
            src = defaultdict(list)

        else:
            surface, morphs = line.rstrip('\n').split('\t')
            morphs = morphs.split(',')
            morph = Morph(surface, morphs[0], morphs[1], morphs[6])
            chunk.append_morph(morph)


if __name__ == '__main__':
    sentence = list()
    for i, line in enumerate(get_neko_list()):
        if i == 5:
            for chunk in line:
                print(chunk)
                sentence.append(chunk.get_string())
            break
