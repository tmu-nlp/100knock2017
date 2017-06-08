import knock30

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
        nouns = []
        for line in mecab_data:
            nouns_phrase = ''
            flag = -99
            flag_continue = 0
            for i, word in enumerate(line):
                if flag_continue == 1:
                    flag_continue = 0
                    continue
                if flag == -99 and word['surface'] == 'の' and word['pos'] == '助詞' and word['pos1'] == '連体化' and i+1 < len(line):
                    nouns_phrase += line[i-1]['surface'] + word['surface'] + line[i+1]['surface']
                    flag = i
                    flag_continue = 1
                elif flag == i-2:
                    if word['surface'] == 'の' and word['pos'] == '助詞' and word['pos1'] == '連体化' and i+1 < len(line):
                        nouns_phrase += word['surface'] + line[i+1]['surface']
                        flag = i
                        flag_continue = 1
                    else:
                        if nouns_phrase != '' and nouns_phrase not in nouns:
                            nouns.append(nouns_phrase)
                            nouns_phrase = ''
                            flag_continue = 0
        with open('../data/neko_nouns_phrase.txt', 'w') as data_out:
            data_out.write(str(nouns))
