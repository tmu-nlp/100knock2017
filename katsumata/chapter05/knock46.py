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
            if morph.getPos() == '記号':
                continue
            temp_phrase += morph.getSurface()    
        #dictはkey:文節番号,value:chunkオブジェクト,文節内に動詞があるかどうか,助詞があるかどうか
        #さらに文節内容を追加
        phrase_dict[i].append(word)
        phrase_dict[i].append(flag_v)
        phrase_dict[i].append(flag_p)
        phrase_dict[i].append(temp_phrase)
    v_base = defaultdict(list)
    #c_depend_list = list()
    #p_depend_list = list()
    for i,word in enumerate(line):
        if not phrase_dict[i][1]:
            continue
        #以下は動詞を見ている    
        morphs = word.getMorphs()
        dst = word.getDst()
        srcs = word.getSrcs()
        #今見ている動詞を確認
        for morph in morphs:
            if morph.getPos() == '動詞':
                v_b = morph.getBase()
                break   #最左動詞
        #ここから先は動詞に対しての係り元を追っていく
        #c_depend_list = list() 
        #p_depend_list = list()
        for src in srcs:
            src = int(src)
            if not phrase_dict[src][2]:
                continue
            depend_phrase = phrase_dict[src][3]
            #p_depend_list.append(phrase_dict[src][3])
            source = phrase_dict[src][0].getMorphs()
            for s in reversed(source):
                if s.getPos() == '助詞':
                    #c_depend_list.append(s.getSurface())
                    depend_case = s.getSurface()
                    break
            depend_tuple = (depend_case, depend_phrase)        
            v_base[v_b].append(depend_tuple)
            #v_base[v_b].append(c_depend_list)
            #v_base[v_b].append(p_depend_list)
        """
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
        """
    for key, value in v_base.items():
        c_list = ''
        d_list = ''
        print('{}'.format(key), end='\t')
        value_s = sorted(value) 
        for w_tuple in value_s:
            c_list += w_tuple[0] + ' '
            d_list += w_tuple[1] + ' '
            #print(w[0]+' '+ w[1], end='')
        print('{}\t{}'.format(c_list, d_list))    
        #print()    
        """    
        for p_0 in value_s[0][0]:
            print('{} '.format(p_0), end='')
        print('\t', end='')
        for p_1 in value_s[0][1]:
            print('{} '.format(p_1),end='')
        print()
        """
    """
    for key, value in v_base.items():
        print('{}'.format(key), end='\t')
        for p in value[0]:
            print('{} '.format(p), end='')
        print('\t', end='')
        for p in value[1]:
            print('{} '.format(p), end='')
        print()
    """    
