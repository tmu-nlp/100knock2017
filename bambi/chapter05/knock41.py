from knock40 import Morph
class Chunk:
    def __init__(self):
        self.srcs = []
        self.dst = -1
        self.morphs = []
    def print_morphs(self, do_remove_punc=False):
        if do_remove_punc:
            return "".join([x.surface for x in self.morphs if x.pos != "記号"]) 
        else:
            return "".join([x.surface for x in self.morphs])
    
class Cabocha:
    def get_sentence(self):
        for s in self.sentences:
            yield s
    def __init__(self):
        #１文をChunkオブジェクトのリスト -> 1 sentencs : list of chunks
        chunks = []
        self.sentences = []
        #file = "test.cabocha"
        file = "neko.txt.cabocha"
        for line in open(file):
            line = line.strip("\n") # must specific \n, if not it will erase whitespace which we treate as moji
            if line == "EOS":
                # get src
                for index, item in enumerate(chunks):
                    dst = chunks[index].dst
                    if dst != -1: #終点じゃない場合のみ
                        chunks[dst].srcs.append(index)
                self.sentences.append(chunks)
                #reset
                chunks = []
            elif line.startswith("*") == True:# * 0 -1D 0/0 0.000000
                parts = line.split(" ")
                item = Chunk()
                item.dst = int(parts[2].replace("D",""))
                chunks.append(item)
            else: # mecab:  表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
                surface, rest = line.split("\t")
                mecab = rest.split(",")
                item = Morph(surface=surface, base=mecab[-3], pos=mecab[0], pos1=mecab[1])
                chunks[-1].morphs.append(item) # -1 for last element of chunks
if __name__ == "__main__":
    chunks = Cabocha().sentences[7]
    print("".join([x.print_morphs() for x in chunks]))
