import knock30

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
        nouns = []
        for line in mecab_data:
            nouns_series = ''
            for word in line:
                if word['pos'] == '名詞':
                    nouns_series += word['surface']
                else:
                    if nouns_series != '':
                        nouns.append(nouns_series)
                        nouns_series = ''
        with open('knock35.txt', 'w') as data_out:
            data_out.write(str(nouns))
