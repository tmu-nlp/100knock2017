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
        flag_noun_s = False
        #word : chunkのオブジェクト
        morphs = word.getMorphs()
        temp_phrase = ''
        case = ''
        flag_first = True
        for morph in morphs:
            #述語を決定する
            #サ変接続名詞があるかどうかを増やす
            if not (flag_noun_s and morph.getSurface() == 'を'):
                flag_noun_s = False
            #print('{} {}'.format(morph.getSurface(), str(flag_noun_s)))    
            if morph.getPos() == '名詞' and morph.getPos1() == 'サ変接続' and flag_first:
                flag_noun_s = True
                flag_first = False
            if morph.getPos() == '動詞':
                flag_v = True
            if morph.getPos() == '助詞' :
                flag_p = True
            if morph.getPos() == '記号':
                continue
            temp_phrase += morph.getSurface()  
        if morph.getPos() == '名詞':
            flag_noun_s = False
        #print ('a'+str(flag_noun_s))
        #dictはkey:文節番号,value:chunkオブジェクト,文節内に動詞があるかどうか,助詞があるかどうか
        #さらに文節内容を追加
        #さらにさらにサ変接続名詞があるかどうか追
        phrase_dict[i].append(word)
        phrase_dict[i].append(flag_v)
        phrase_dict[i].append(flag_p)
        phrase_dict[i].append(temp_phrase)
        phrase_dict[i].append(flag_noun_s)
    v_base = defaultdict(list)
    c_depend_list = list()
    p_depend_list = list()
    for i, word in enumerate(line):
        if not phrase_dict[i][4]:
            continue 
        #ここから先は1文中にサ変接続名詞+'を'が存在
        #この名詞の係り先が動詞かどうか
        dst_n =  int(word.getDst())
        if not phrase_dict[dst_n][1]:
            break
        #サ変名詞+'を'+動詞の表層系を入れる
        v_morphs = phrase_dict[dst_n][0].getMorphs()
        for morph in v_morphs:
            if morph.getPos() == '動詞':    #最左動詞のみ使う
                v_surf = morph.getBase()
                break
        v_surf = phrase_dict[i][3] + v_surf 
        #ここから先は動詞(述語)に対しての係り元を追っていく
        srcs = phrase_dict[dst_n][0].getSrcs()
        """
        c_list : 係り元助詞リスト,case
        p_list : 係り元文節リスト,phrase
        """
        c_depend_list = list()
        p_depend_list = list()
        for src in srcs:
            src = int(src)
            if src == i:
                continue
            if not phrase_dict[src][2]:
                continue
            depend_phrase = phrase_dict[src][3]    
            #p_depend_list.append(phrase_dict[src][3])
            source = phrase_dict[src][0].getMorphs()
            for s in reversed(source):
                if s.getPos() == '助詞':
                    depend_case = s.getSurface()
                    #c_depend_list.append(s.getSurface())
                    break
            depend_tuple = (depend_case, depend_phrase)
            v_base[v_surf].append(depend_tuple)        
            #v_base[v_surf].append(c_depend_list)
            #v_base[v_surf].append(p_depend_list)
    for key, value in v_base.items():
        c_list = ''
        d_list = ''
        value_s = sorted(value)
        for w_tuple in value_s:
            c_list += w_tuple[0] + ' '
            d_list += w_tuple[1] + ' '
        print('{}\t{}\t{}'.format(key,c_list,d_list))
    """        
    for key, value in v_base.items():
        print('{}'.format(key), end='\t')
        for p_0 in value[0]:
            print('{} '.format(p_0), end='')
        print('\t', end='')
        for p_1 in value[1]:
            print('{} '.format(p_1), end='')
        print() 
    """    
