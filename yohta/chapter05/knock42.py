#from collections import defaultdict
from knock40 import Morph
from knock41 import func41,Chunk

#if __name__ =='__main__':
for line in func41():
    for b in line:
        if b.getDst() != -1:
            ingword = b.getSurword()
            edword = line[b.getDst()].getSurword()
            if len(ingword) > 0 and len(edword) > 0:
#            if ingword != None and edword != None:
#                ingword = ingword.strip('。')
                print('{}\t{}'.format(ingword,edword))

"""こっちでもできる（#付きのgetSurword()使用:新しい記号を見つけるたびに追加する必要あり）
                ingword = ingword.strip(r'。|、|「|」')
                edword = edword.strip(r'。|、|「|」')
#                edword = edword.strip('、')
                print('{}\t{}'.format(ingword,edword))
#                   sentence.append(ch.getMorphs_1())
"""
