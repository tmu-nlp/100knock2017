from knock41 import Chunk
from knock41 import cabocha_data

for line in cabocha_data():
    for chunk in line:
        if chunk.dst == -1:
            continue
        flag = False
        for morph in chunk.morphs:
            if morph.pos == '名詞':
                flag = True
        if flag == True:
            for morph_v in line[chunk.dst].morphs:
                if morph_v.pos == '動詞':
                     print(chunk.get_word_only() + '\t' +  line[chunk.dst].get_word_only())
                     break
               # if dst[morph[pos]] == 動詞

                

