from knock40 import Morph
from collections import defaultdict
class Chunk:
    def _init_(self, morphs, dst, srcs, index):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
        self.index = index

def func2():
    with open('neko.txt.cabocha', 'r') as f:
        m_tmp = list()
        c_tmp = list()
        chunk = Chunk()
        flag = False
        relate = defaultdict(lambda: list())
        for line in f:
            line = line.replace(' ', ',')
            line = line.replace('D', '')
            words = (line.replace('\t', ',')).strip().split(',')
            kts = Morph()
            if(words[0] != '*' and words[0] != 'EOS'): #形態素解析をリストに加える
                kts.surface = words[0]
                kts.base = words[7]
                kts.pos = words[1]
                kts.pos1 = words[2]
                m_tmp.append(kts)

            elif(words[0] == 'EOS'):
                chunk.morphs = m_tmp #形態素解析のデータを保存
                m_tmp = list()
                c_tmp.append(chunk)
                yield c_tmp
                relate = defaultdict(lambda: list())
                c_tmp = list()
                flag = False

            elif(words[0] == '*'):
                if flag:
                    chunk.morphs = m_tmp #形態素解析のデータを保存
                    m_tmp = list()
                    c_tmp.append(chunk)
                    chunk = Chunk()
                flag = True
                chunk.dst = words[2]
                relate[words[2]].append(words[1])
                chunk.srcs = relate[words[1]]
                chunk.index = words[1]


if __name__ == '__main__':
    for i, x in enumerate(func2()):
        if(i == 7):
            for line in x:
                for morph in line.morphs:
                    print(morph.surface)
                print('index：', line.index)
                print('係り先：', line.dst)
                print('係り元：', line.srcs)
            break
