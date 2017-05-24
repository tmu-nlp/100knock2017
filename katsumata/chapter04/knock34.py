from knock30 import make_morpheme_list

morpheme_list = make_morpheme_list()
b_of_a = list()
for line in morpheme_list:
    """
    flag_noun1 = False
    flag_noun2 = False
    """
    flag_no = False
    flag_noun = False
    
    for word in line:
        if flag_no and word['pos'] == '名詞':
            b_of_a.append('{}の{}'.format(noun, word['surface']))
            flag_noun = False
            flag_no = False
        if word['pos'] == '名詞':
            noun = word['surface']
            flag_noun = True
        if word['surface'] == 'の' and word['pos'] == '助詞' and flag_noun:
            flag_no = True

        ###以下のプログラムだとAのBのCがそのまま出てしまう
        """
        if word['pos'] == '名詞' and not flag_no:
            #一つ目の名詞
            flag_noun1 = True
            temp_words = ''
            noun_word1 = word['surface']
            temp_words += noun_word1
        if flag_noun1:
            if word['surface'] == 'の' and word['pos'] == '助詞':
                #flag_noが”名詞の”でたつ
                flag_no = True
                temp_words += word['surface']
                continue
        if flag_no:
            noun_word2 = word['surface']
            temp_words += noun_word2
            b_of_a.append(temp_words)
            flag_no = False
        """    
print (b_of_a)            

