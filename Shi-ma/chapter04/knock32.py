import knock30

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
    verbs = []
    for line in mecab_data:
        for word in line:
            if word['pos'] == '動詞':
                if not word['base'] in verbs:
                    verbs.append(word['base'])
    with open('../data/neko_verbs_base.txt', 'w') as data_out:
        data_out.write(str(verbs))
