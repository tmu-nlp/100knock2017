import knock30

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
    nouns = []
    for line in mecab_data:
        for word in line:
            if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
                if not word['surface'] in nouns:
                    nouns.append(word['surface'])
    with open('../data/neko_nouns.txt', 'w') as data_out:
        data_out.write(str(nouns))
