class Morph():
    def __init__(self,surface,morph):
        self.surface = surface
        self.base = morph[6]
        self.pos = morph[0]
        self.pos1 = morph[1]

    def get_morph(self):
        return (self.surface, self.base, self.pos, self.pos1)

    def get_surface(self):
        return self.surface

    def get_base(self):
        return self.base

    def get_pos(self):
        return self.pos

    def get_pos1(self):
        return self.pos1

class Chank():
    def __init__(self,dst,srcs):
        self.morphs = list()
        self.dst = dst
        self.srcs = srcs

    def get_chank(self):
        return (self.morphs,self.dst,self.srcs)

    def get_morphs(self):
        return (self.morphs)

    def get_dst(self):
        return (self.dst)

    def get_srcs(self):
        return (self.srcs)

    def set_morphs(self,morph):
        self.morphs.append(morph)
