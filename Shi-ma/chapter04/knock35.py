import knock30

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
        nouns = []
        for line in mecab_data:
            nouns_series = ''
            flag = -99
            for i, word in enumerate(line):
                if word['pos'] == '名詞' and (flag == -99 or flag == i-1):
                    nouns_series += word['surface']
                    flag = i
                elif word['pos'] != '名詞' and flag == i-1 and nouns_series not in nouns:
                    nouns.append(nouns_series)
        with open('../data/neko_nouns_series.txt', 'w') as data_out:
            data_out.write(str(nouns))
