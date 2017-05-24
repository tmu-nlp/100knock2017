from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib as mpl

def ktskaiseki():
    result = list()
    text = list()
    with open('neko.mecab.txt', 'r') as f:
        for line in f:
            line = ','.join(line.split()).split(',')
            if(line[0] != 'EOS'):
                tmpdict = dict()
                tmpdict['surface'] = line[0]
                tmpdict['base'] = line[7]
                tmpdict['pos'] = line[1]
                tmpdict['pos1'] = line[2]
                text.append(tmpdict)
            elif(line[0] == 'EOS'):
                if(len(text) > 0):#最後に出てくるからのリストがイラついたため
                    result.append(text)
                    text = list()
        return result

if __name__ == '__main__':
    kts = ktskaiseki()
    count = defaultdict(lambda : 0)
    for i in range(len(kts)):
        for j in range(len(kts[i])):
            count[kts[i][j]['surface']] += 1

    left = list()
    labels = list()
    height = list()
    rank = 0
    mpl.rcParams['font.family'] = 'AppleGothic'
    for k, v in sorted(count.items(), key = lambda x:x[1], reverse = True):
        rank += 1
        left.append(rank)
        labels.append(k)
        height.append(v)

    plt.hist(height, bins = 100, log = 1)
    #plt.bar(left, height, tick_label = labels, aline = 'center')

    plt.show()
