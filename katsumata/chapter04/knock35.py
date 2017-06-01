from knock30 import make_morpheme_list
morpheme_list = make_morpheme_list()

noun_list = list()
for line in morpheme_list:
    temp_word = ''
    noun_flag = False
    for word in line:
        if word['pos'] == '名詞':
            temp_word += word['surface'] + ' '
            noun_flag = True
        else:
            if noun_flag and len(temp_word.strip().split(' ')) > 1:
                noun_list.append(''.join(temp_word.strip().split()))
                noun_flag = False
            temp_word = ''    
print (noun_list)            
