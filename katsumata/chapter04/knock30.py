def make_morpheme_list():
    morpheme_list = list()

    keys = ['surface', 'base', 'pos', 'pos1']
    indexes = [0,7,1,2]
    """
    index
    0:表層形
    1:品詞
    2:品詞細分類1
    7:原形
    """
    temp_dict = dict()
    temp_list = list()
    with open('neko.txt.mecab', 'r') as neko:
        for line in neko:
            temp_dict = dict()
            line = line.replace('\t',',')
            words = line.strip().split(',')
            if words[0] != 'EOS':
                for key, index in zip(keys, indexes):
                    temp_dict[key] = words[index]
                temp_list.append(temp_dict)
            else:
                if len(temp_list) != 0:
                    morpheme_list.append(temp_list)
                    temp_list = list()
    return morpheme_list

if __name__ == '__main__':
    morpheme_list = make_morpheme_list()
    #print (morpheme_list)
    for value in morpheme_list:
        print (value)
