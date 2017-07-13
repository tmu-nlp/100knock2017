from knock41 import Chunk
from knock41 import cabocha_data

for line in cabocha_data():
    #print(line)
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
                #print(morph_srcs)
                for morphs in line[morph_srcs].morphs:
                    if morphs.pos1 == '格助詞':
                        L.append([morphs.surface, line[morph_srcs].get_word_only()])
                        # print(line[morph_srcs].get_word_only())

            if len(L) > 0:
              
                particle, phrase = list(zip(*L))

                print('{}\t{}\t{}'.format(verb, ' '.join(particle), ' '.join(phrase)))
#                for morph_p in morph:
                
                   
                        #print(chunk.srcs)
               # print(chunk.get_word_only())
                #print(morph.base + '\t' + str(chunk.srcs))
               
