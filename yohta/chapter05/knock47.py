from knock41 import func41,Chunk
from knock40 import Morph

N =100  #参照列数（EOSの数とは無関係）
counter = 0
for line in func41():
    if counter > N:
        break
    for b in line:
        #ingnotdouble初期化、bのmorphのPosを参照、動詞であれば原形（？）をingnotdoubleに代入
        ingnotdouble = ''
        for morph in b.getMorphs():
            if morph.getPos1() == 'サ変接続':
                ingnotdouble = morph.getBase() + 'をする'
#               print(morph.getBase())
#               ingnotdouble = morph.getBase()
        if ingnotdouble == '':
            continue

        edword = list()
        edwords = list()
        for srcs in b.getSrcs():
            smorphs = line[srcs].getMorphs()
#            print(smorphs[-1])
#               --0で名詞、動詞、副詞
#               --(-1)で助詞、副詞、記号
#               -->句は主格・主辞（smorphs[0]）の部分と他の要素（smorphs[-1]）より成る
#            if smorphs[-1].getPos() =='助詞':
            if smorphs[-1].getPos() == '助詞':
                edword.append(smorphs[-1].getBase())
#                print(line[srcs].getSurword())
                edwords.append(line[srcs].getSurword())
#            for i in range(len(smorphs)):
#                if smorphs[i].getPos() != '記号':
#                    smorph = line[srcs].
#                    edwords.append(smorphs[i].getBase())

#                    edword = ''.join(edword)
#                print(smorphs)
        if len(edword) > 0:
            posposi = ' '.join(edword)
            ed = ' '.join(edwords)
            print('{}\t{}\t{}'.format(ingnotdouble,posposi,ed))
    counter += 1
