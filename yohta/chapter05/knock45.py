from knock40 import Morph
from knock41 import func41,Chunk
#from collections import defaultdict

"""
#if __name__ =='__main__':
N = 10
counter = 0
#ingnotdouble = list()
for line in func41():
#    posposi = ''
    if counter > N:
        break
    for b in line:
    #    posposi = ''
        if b.getDst() != -1:
            if '動詞' in [morph.getPos() for morph in b.getMorphs()] and '助詞' in [morph.getPos() for morph in line[b.getDst()].getMorphs()]:
                ingword = b.getBaseword()
                edword = line[b.getDst()].getBaseword()
                edlist = b.getSrcs()
#                posposi = ' '.join(edword)
#                if edlist != []:
#                    continue
#        for i in edlist:
#                    posposi = ' '.join(edword)
                if len(ingword) > 0 and len(edword) > 0:
                    print('{}\t{}'.format(ingword,edlist))
    counter += 1
"""
"""
                    words[ingword] = ingword + ' ' + edword
                    ingnotdouble.append(ingword)
                    for i in range(len(words[ingword])):
                        words[ingword].split(' ')
                        if words[ingword][0] in ingnotdouble:
#                if ingword != None and edword != None:
#                ingword = ingword.strip('。')
                        print('{}\t{}'.format(ingword,edword))
"""
N = 30  #参照列数（EOSの数とは無関係）
counter = 0
for line in func41():
    if counter > N:
        break
    for b in line:
        #ingnotdouble初期化、bのmorphのPosを参照、動詞であれば原形（？）をingnotdoubleに代入
        ingnotdouble = ''
        for morph in b.getMorphs():
            if morph.getPos() == '動詞':
                ingnotdouble = morph.getBase()
        if ingnotdouble == '':
            continue

        edword = list()
        for srcs in b.getSrcs():
            smorphs = line[srcs].getMorphs()
#            print(smorphs[-1])
#               --0で名詞、動詞、副詞
#               --(-1)で助詞、副詞、記号
#               -->句は主格・主辞（smorphs[0]）の部分と他の要素（smorphs[-1]）より成る
            if smorphs[-1].getPos() =='助詞':
                edword.append(smorphs[-1].getBase())
        if len(edword) > 0:
            posposi = ' '.join(edword)
            print('{}\t{}'.format(ingnotdouble,posposi))
    counter += 1

"""
edword = 助詞
posposi = その動詞にかかっている助詞群
print ingnotdouble,posposi

b = knock41のchunk class
"""
