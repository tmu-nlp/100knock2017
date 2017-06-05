class Chunk:
    
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    
    def getMorphs(self):
        return self.morphs
    def getDst(self):
        return self.dst
    def getSrcs(self):
        return self.srcs
