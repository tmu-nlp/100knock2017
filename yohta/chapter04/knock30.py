"""
split(,)で
表層 = list[0]
基本 = list[7]
品詞 = list[1]
品詞細分類 = list[2]
"""

def map_make(ins_f_1):
    map30 = {}
    line = ins_f_1.replace(',','\t')
    neko = line.split('\t')
    map30['surface'] = neko[0]
    map30['base'] = neko[7]
    map30['pos'] = neko[1]
    map30['pos1'] = neko[2]
#    print(map30)
    return map30

def list_make(ins_f_2):
    list_1 = []
    list_2 = []
    for line in ins_f_2:
        if line != 'EOS\n':
            list_1.append(map_make(line))
        elif line == 'EOS\n':
            list_2.append(list_1)
#            list_2.append('\n')
            list_1 = []

#    print(list_2)
    return(list_2)

if __name__ == '__main__':
    with open('../data/neko.txt.mecab','r') as f_r:
        print(list_make(f_r))
#        with open('../data/nekolist.txt','w') as f_w:
#            f_w.write(str(list_make(f_r)) + '\n')
