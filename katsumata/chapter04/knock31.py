from knock30 import make_morpheme_list

morpheme_list = make_morpheme_list()
for line in morpheme_list:
    for word in line:
        if word['pos'] == '動詞':
            print (word['surface'])
