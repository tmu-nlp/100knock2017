from knock41 import make_chunk_list
chunk_list = make_chunk_list()
for line in chunk_list:
    for word in line:
        morphs = word.getMorphs()
        dst = word.getDst()
        for morph in morphs:
            if morph.getPos() == '記号':
                continue
            if dst == '-1':
                subject = ''
                break
            print ('{}'.format(morph.getSurface()), end='')
        if dst != '-1':
            subject = ''
            for a in line[int(dst)].getMorphs():
                if a.getPos() == '記号':
                    continue
                subject += a.getSurface()
        print ('\t{}'.format(subject))
    print ('')
