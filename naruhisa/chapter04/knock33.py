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
    for i in range(len(kts)):
        for j in range(len(kts[i])):
            if(kts[i][j]['pos'] == '名詞' and kts[i][j]['pos1'] == 'サ変接続'):
                print(kts[i][j])
