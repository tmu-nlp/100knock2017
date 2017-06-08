from knock41 import make_chunk_list
from collections import defaultdict
#名詞のタプルを作成
def binoun(noun_list):
    noun_list2 = list()
    for i in noun_list:
        for j in reversed(noun_list):
            if i == j :
                break 
            noun_list2.append((i,j))
    return noun_list2        

line_number = int(input('何行目のパスが欲しいですか:'))

chunk_list = make_chunk_list()
phrase_dict = defaultdict(list)

for i, word in enumerate(chunk_list[line_number]):
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

noun_list = list()
for i in range(len(chunk_list[line_number])):
    if phrase_dict[i][2]:
        noun_list.append(i)
binoun_list = binoun(noun_list)
"""
flag_1 : 根に至るまでに係り受けパスが見つかった時
これがfalseのままだったら、もう一つの場合(場合2)
"""
for nouns in binoun_list:
    #nouns[0]から始める,つまりnouns[0]のパスを追っていく
    dst = int(phrase_dict[nouns[0]][0].getDst()) 
    if dst == -1:
        break
    pass_list = list()
    pass_num = list()
    flag_1 = False
    while True:
        if dst == nouns[1]:
            flag_1 = True
            break
        if dst == -1:
            break
        pass_list.append(phrase_dict[dst][1])
        pass_num.append(dst)
        dst = int(phrase_dict[dst][0].getDst()) 
    sources = phrase_dict[nouns[0]][0].getMorphs()
    temp_source_x = ''
    for source in sources:
        if source.getPos() == '名詞':
            temp_source_x += 'X'
        else:
            if source.getPos() == '記号':
                continue
            temp_source_x += source.getSurface()
    pass_list.insert(0, temp_source_x)
    if flag_1:
        pass_list.append('Y')
        print(' -> '.join(pass_list))
        continue
    #以下,場合2について,Xは根まで見ている    
    dst = int(phrase_dict[nouns[1]][0].getDst())
    pass_list_y = list()
    while True:
        #ここではyに関する探索を行う
        word = phrase_dict[dst][1]    
        if dst in pass_num:
            co_dst = dst
            break
        pass_list_y.append(phrase_dict[dst][1])
        dst = int(phrase_dict[dst][0].getDst())
    sources = phrase_dict[nouns[1]][0].getMorphs()
    temp_source = ''
    for source in sources:
        if source.getPos() == '名詞':
            temp_source += 'Y'
        else:
            if source.getPos() == '記号':
                continue
            temp_source += source.getSurface()
    pass_list_y.insert(0, temp_source)
    pass_list_x = list()
    pass_list_x.append(temp_source_x)
    for i in pass_num:
        if i == co_dst:
            break
        pass_list_x.append(phrase_dict[i][1])
    print(' -> '.join(pass_list_x), end=' | ')
    print(' -> '.join(pass_list_y), end=' | ')
    print(word)

