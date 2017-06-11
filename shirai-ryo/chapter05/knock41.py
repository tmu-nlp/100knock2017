from collections import defaultdict
from knock40 import Morph


class Chunk:
    def __init__(self, dst, srcs):
    #このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）
        self.morphs = []
        self.dst = dst
        self.srcs = srcs

    def get_chunk(self):
        return [self.morphs, self.dst, self.srcs]

    def get_surface_list(self): #get_surfaceの名前を40で使うことにしたので名前に_listを付け加えた
        surface_list = []
        for w in self.morphs:
            surface_list.append(w.surface)
        return surface_list

    def get_dst(self):
        return self.dst

    def get_srcs(self):
        return self.srcs

    def get_word_only(self): #42で追加
        return "".join([morph.get_surface() for morph in self.get_word_only_morphs()])

    def get_word_only_morphs(self): #42で追加
        return [morph for morph in self.morphs if morph.get_pos() != "記号"]
        # 記号をはじく
        # morphは「for i in なんちゃら」の i みたいなもの

    def get_morphs(self): #43で追加
        return self.morphs

def cabocha_data():
    with open("neko.txt.cabocha", "r") as text:
        k_list = [] #　全文
        n_list = [] #　一文

        my_dict = defaultdict(list) #リスト型の空の辞書ができる  # src
        for line in text:
            words = line.strip("\n").replace("\t", ",").split(",")
            if words[0].startswith("*"):
                words = words[0].split()
                index = int(words[1])
                kakari = int(words[2].strip("D"))
                my_dict[kakari].append(index)
                #係り先の番号に係り元のインデックスを入れる
                chunk = Chunk(kakari, my_dict[kakari])
                n_list.append(chunk)
            elif line.startswith('EOS'):
                if len(n_list) > 0:
                    k_list.append(n_list)
                n_list = []
                my_dict = defaultdict(list) #初期化
            else:
                morphs = Morph(words[0], words[7], words[1], words[2])
                chunk.morphs.append(morphs)
    return k_list

if __name__ == "__main__":
    for chunk in cabocha_data()[7]:
        print(chunk.get_surface_list(), chunk.dst)
