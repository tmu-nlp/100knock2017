from knock40 import Morph
from knock41 import func41,Chunk

#if __name__ =='__main__':
for line in func41():
    for b in line:
        if b.getDst() != -1:
            if '名詞' in [morph.getPos() for morph in b.getMorphs()] and '動詞' in [morph.getPos() for morph in line[b.getDst()].getMorphs()]:
                ingword = b.getSurword()
                edword = line[b.getDst()].getSurword()
                if len(ingword) > 0 and len(edword) > 0:
#            if ingword != None and edword != None:
#                ingword = ingword.strip('。')
                    print('{}\t{}'.format(ingword,edword))
