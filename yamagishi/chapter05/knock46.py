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
        particles_chunk = list()
        for src in chunk.get_srcs():
            src_morph = line[src].get_morphs()
            if len(src_morph) > 0 and src_morph[-1].get_pos() =='助詞':
                particles.append(src_morph[-1].get_base())
                particles_chunk.append(line[src].get_word_only())
        if len(particles) > 0:
            print('{}\t{}\t{}'.format(verb, ' '.join(particles), ' '.join(particles_chunk)))