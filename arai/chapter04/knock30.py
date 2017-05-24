def mecab_data():
    with open('neko.txt.mecab') as text:
        mlist = []
        Mlist = []
        for line in text:
            word = line.strip('\n').replace('\t',',').split(',')
            if word[0]=='EOS':
                if len(mlist) > 0:
                    Mlist.append(mlist)
                mlist = []
                
            else:

                mkeys = {'surface': word[0], 'base': word[7], 'pos':word[1] ,'pos1':word[2]}
                mlist.append(mkeys)
    return Mlist

if __name__=='__main__':
    print(mecab_data())

