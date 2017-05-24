from knock30 import make_morpheme_list

morpheme_list = make_morpheme_list()
count = 0
for line in morpheme_list:
    for word in line:
        if word['pos1'] == 'サ変接続':
            #print (word['pos'])
            print (word['surface'])
            if word['pos'] != '名詞':
                count += 1
print ('count = {}'.format(count))                
