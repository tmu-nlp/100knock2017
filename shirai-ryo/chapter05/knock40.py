class Morph:
    #これはクラスのルールを決めている
    def __init__(self, surface, base, pos, pos1):   # 初期化： インスタンス生成時に自動的に呼ばれる
        #表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def get_morph(self):
        return [self.surface, self.base, self.pos, self.pos1]

    def get_surface(self):
        return self.surface

    def get_base(self):
        return self.base

    def get_pos(self):
        return self.pos

    def get_pos1(self):
        return self.pos1

if __name__ == "__main__":
    #インポートでは起こらない処理を書く
    with open("neko.txt.cabocha", "r") as text:
        k_list = []
        n_list = []
        for line in text:
            words = line.strip("\n").replace("\t", ",").split(",")
            if line.startswith("*"):
                pass
            elif line.startswith('EOS'):
                if len(n_list) > 0:
                    k_list.append(n_list)
                n_list = []
            else:
                morph = Morph(words[0], words[7], words[1], words[2])
                n_list.append(morph)
        for m in k_list[2]:
            print(m.get_morph())
