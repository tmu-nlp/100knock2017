from knock41 import Chunk
from knock41 import cabocha_data

for line in cabocha_data():
    for chunk in line:
        flag = False
        L = []
        #print(chunk.srcs)
        for morph in chunk.morphs:
            if morph.pos == '動詞':
                verb = morph.base
                flag = True
        if flag == True:
            for morph_srcs in chunk.srcs:
                for morphs in line[morph_srcs].morphs:
                    if morphs.pos1 == '格助詞':
                        L.append(morphs.surface)

            if len(L) > 0:
                print('{}\t{}'.format(verb, ' '.join(L)))
#                for morph_p in morph:
                
                   
                        #print(chunk.srcs)
               # print(chunk.get_word_only())
                #print(morph.base + '\t' + str(chunk.srcs))
               
