from collections import defaultdict
from knock40 import Morph

class Chunk:
    def __init__(self,dst,index,srcs):
        self.morphs = list()
        self.dst = dst
        self.index = index
        self.srcs = srcs

    def __str__(self):
        return 'index:{}\t\tdst:{}\t\tsurface:{}'.format(self.getIndex(),self.getDst(),self.getMorphs_1())

    def getMorphs(self):
        return self.morphs
    def getDst(self):
        return self.dst
    def getSrcs(self):
        return self.srcs
    def getIndex(self):
        return self.index

#文頭の記号だけ参照する（文中は見れない）
#    def getSurword(self):
#        for m in self.morphs:
#            if m.getPos() != '記号':
#                return ''.join([m.getSurface() for m in self.morphs])

    def getBaseword(self):
        return ''.join([m.getBase() for m in self.morphs if m.getPos() == '動詞'])

#    def getOnlybase(self):
#        return [m for m in self.morphs if m.getPos() != '記号']

    def getNoun(self):
        return any(m.getPos() == '名詞' for m in self.morphs)

#---内包表記でknock42実装
    def getSurword(self):
        return ''.join([m.getSurface() for m in self.getOnlysur()])

    def getOnlysur(self):
        return [m for m in self.morphs if m.getPos() != '記号']
#---------

    def getMorphs_1(self):
        return ''.join([m.getSurface() for m in self.morphs])

#    def morphAppending(self,morph):
#        morphs = []
#        morphs.append(morph)
#        self.morphs

    def morphAppending(self,morph):
        self.morphs.append(morph)
#        self.morphs

def func41():
#    sentence_counter = 1
    sentence = list()
    store = defaultdict(list)
    with open('../data/neko.txt.cabocha','r') as neko:
        for line in neko:
            if line.startswith('*'):
                line.replace(',',' ')
                line.replace('\t',' ')
                element = line.rstrip('\n').split()
                ind = int(element[1])
                num = int(element[2].strip('D')) #dst:掛かり先のint
                store[num].append(ind) #store:掛かり元のリスト
                b = Chunk(num,ind,store[ind])
                sentence.append(b)

            elif line.startswith('EOS'):
                if len(sentence) > 0:
                    yield sentence
                sentence = list()
                store = defaultdict(list)
#            sentence_counter += 1

            else:
                word,morphs = line.rstrip('\n').split('\t')
                morphs = morphs.split(',')
#                line.replace(',',' ')
#                line.replace('\t',' ')
#                words = line.rstrip('\n').split()
#                if len(words) > 6:
#                print(1)
                a = Morph(word,morphs[6],morphs[0],morphs[1])
#                a = Morph(words[0],words[7],words[1],words[2])
                b.morphAppending(a)
#                    print(a.getSurface())


if __name__ =='__main__':
    print('文節番号'+'\t'+'掛かり先'+'\t'+'表層形')
#    sentence = list()
    for num,line in enumerate(func41()):
        if num == 5:
            for chunk in line:
                print(chunk)
#                sentence.append(ch.getMorphs_1())
            break
