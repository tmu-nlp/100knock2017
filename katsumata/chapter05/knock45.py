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
        for morph in morphs:
            if morph.getPos() == '動詞':
                flag_v = True
            if morph.getPos() == '助詞':
                flag_p = True
        #dictはkey:文節番号,value:chunkオブジェクト,文節内に動詞があるかどうか,助詞があるかどうか
        phrase_dict[i].append(word)
        phrase_dict[i].append(flag_v)
        phrase_dict[i].append(flag_p)
    v_base = defaultdict(list)
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
        for src in srcs:
            src = int(src)
            if not phrase_dict[src][2]:
                continue
            source = phrase_dict[src][0].getMorphs()
            for s in reversed(source):
                if s.getPos() == '助詞':
                    v_base[v_b].append(s.getSurface())
                    break   #最右助詞

                
        """
        for src in srcs:
            flag_left_v = False
            src = int(src)
            if phrase_dict[i][1] and phrase_dict[src][2]:
                for morph in morphs:
                    if morph.getPos() == '動詞':
                        if flag_left_v:
                            continue
                        temp_morph = phrase_dict[src][0].getMorphs()
                        flag_right_c = False
                        for m in reversed(temp_morph):
                            #print ('係り元の形態素解析が開始')
                            if m.getPos() == '助詞':
                                if flag_right_c:
                                    continue 
                                v_base[morph.getBase()].append(m.getSurface())
                                flag_right_c = True
                            #print ('係り元の形態素解析が終了')        
                        flag_left_v = True
        """                
    for key, value in v_base.items():
        print('{}'.format(key), end='\t')
        for p in sorted(value):
            print('{} '.format(p), end='')
        print()   
