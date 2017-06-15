from knock41 import Chunk, get_neko_list

for line in get_neko_list():
    for chunk in line:
        verb = ''
        for morph in chunk.get_morphs():
            if morph.get_pos() == '動詞':
                verb = morph.get_base()
        if verb == '':
            continue

        particles = list()
        for src in chunk.get_srcs():
            src_morph = line[src].get_morphs()
            if src_morph[-1].get_pos() =='助詞':
                particles.append(src_morph[-1].get_base())
        if len(particles) > 0:
            print('{}\t{}'.format(verb, ' '.join(sorted(particles))))
