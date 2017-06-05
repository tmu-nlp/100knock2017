from knock41 import make_chunk_list
from collections import defaultdict
chunk_list = make_chunk_list()
        
for line in chunk_list:
    #flag_vp = False
    #文節区切りで保存しておく
    phrase_dict = defaultdict(list)
    for i,word in enumerate(line):
        flag_v = False
        flag_p = False
        #word : chunkのオブジェクト
        morphs = word.getMorphs()
        temp_phrase = ''
        for morph in morphs:
            if morph.getPos() == '動詞':
                flag_v = True
            if morph.getPos() == '助詞':
                flag_p = True
            temp_phrase += morph.getSurface()    
        #dictはkey:文節番号,value:chunkオブジェクト,文節内に動詞があるかどうか,助詞があるかどうか
        #さらに文節内容を追加
        phrase_dict[i].append(word)
        phrase_dict[i].append(flag_v)
        phrase_dict[i].append(flag_p)
        phrase_dict[i].append(temp_phrase)
    v_base = defaultdict(list)
    c_depend_list = list()
    p_depend_list = list()
    for i,word in enumerate(line):
        morphs = word.getMorphs()
        dst = word.getDst()
        srcs = word.getSrcs()
        for src in srcs:
            flag_left_v = False
            src = int(src)
            if phrase_dict[i][1] and phrase_dict[src][2]:
                p_depend_list.append(phrase_dict[src][3])
                for morph in morphs:
                    #係り先の形態素を見ている
                    if morph.getPos() == '動詞':
                        if flag_left_v:
                            continue
                        #動詞の形態素を見ている
                        #係り元の形態素列を見ている
                        temp_morph = phrase_dict[src][0].getMorphs()
                        flag_right_c = False
                        for m in reversed(temp_morph):
                            if m.getPos() == '助詞':
                                if flag_right_c:
                                    continue
                                #if not flag_left_v:
                                c_depend_list.append(m.getSurface())
                                flag_right_c = True
                                #print ('append : {}'.format(m.getSurface()))
                                #v_base[morph.getBase()].append(m.getSurface())
                        
                        #if not flag_left_v:
                        v_base[morph.getBase()].append(c_depend_list)
                        v_base[morph.getBase()].append(p_depend_list)
                        flag_left_v = True
        c_depend_list = list()
        p_depend_list = list()

    for key, value in v_base.items():
        print('{}'.format(key), end='\t')
        for p in value[0]:
            print('{} '.format(p), end='')
        print('\t', end='')
        for p in value[1]:
            print('{} '.format(p), end='')
        print()   
