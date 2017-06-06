from knock41 import make_chunk_list
from collections import defaultdict

line_number = int(input('何行目のパスが欲しいですか:'))

chunk_list = make_chunk_list()
phrase_dict = defaultdict(list)

for i,word in enumerate(chunk_list[line_number]):
    flag_noun = False
    morphs = word.getMorphs()
    temp_str = ''
    for morph in morphs:
        if morph.getPos() == '名詞':
            flag_noun = True
        if morph.getPos() == '記号':
            continue
        temp_str += morph.getSurface()
    phrase_dict[i].append(word)
    phrase_dict[i].append(temp_str)
    phrase_dict[i].append(flag_noun)

for i,word in enumerate(chunk_list[line_number]):
    if not phrase_dict[i][2]:
        continue
    pass_list = list()    
    #以下、名詞が見つかった時の動作   
    dst = int(phrase_dict[i][0].getDst())
    if dst == -1:
        break
    pass_list.append(phrase_dict[i][1])
    while True:
        if dst == -1:
            break
        pass_list.append(phrase_dict[dst][1])
        dst = int(phrase_dict[dst][0].getDst())
    print (' -> '.join(pass_list))    
