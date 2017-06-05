from knock41 import make_chunk_list
chunk_list = make_chunk_list()
for line in chunk_list:
    for word in line:
        morphs = word.getMorphs()
        dst = word.getDst()
        flag_np = False
        flag_vp = False
        np = ''
        for morph in morphs:
            if morph.getPos() == '名詞':
                flag_np = True
            elif not flag_np:
                break
            if morph.getPos() == '記号':
                continue
            np += morph.getSurface()    
        if dst != '-1':
            subject = ''
            flag_vp = False
            for a in line[int(dst)].getMorphs():
                if a.getPos() == '動詞':
                    flag_vp = True
                elif not flag_vp:
                    break
                if a.getPos() == '記号':
                    continue
                subject += a.getSurface()
        if flag_vp and flag_np:        
            print ('{}\t{}'.format(np,subject))
    #print ('')
