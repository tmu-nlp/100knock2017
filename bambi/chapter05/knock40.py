class Morph:
    # dst_index, own_index will use for Chunk class in knock 41
    def __init__(self, surface, base, pos, pos1, dst_index=None, own_index=None):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        self.dst_index = dst_index
        self.own_index = own_index
        
    def print_self(self):
        print("{},{},{},{}".format(self.surface,self.base,self.pos,self.pos1))
        
mecabs = []
for line in open("neko.txt.cabocha"):
    line = line.strip("\n") # must specific \n, if not it will erase whitespace which we treat it as moji
    if line != "EOS" and line.startswith("*") == False: # not end of sentense and * 0 -1D 0/0 0.000000 -> kind of relationship map
        parts = line.split("\t")
        surface = parts[0]
        mecab = parts[1].split(",")
        item = Morph(surface=surface, base=mecab[-3], pos=mecab[0], pos1=mecab[1])
        mecabs.append(item)
        
if __name__ == "__main__":
    mecabs[3].print_self()
