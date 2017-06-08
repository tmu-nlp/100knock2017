class Morph:
    
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def getSurface(self):
        return self.surface
    def getBase(self):
        return self.base
    def getPos(self):
        return self.pos
    def getPos1(self):
        return self.pos1
    
    def setSurface(self, surface):
        self.surface = surface
    def setBase(self, base):
        self.base = base
    def setPos(self, pos):
        self.pos = pos
    def setPos1(self, pos1):
        self.pos1 = pos1
