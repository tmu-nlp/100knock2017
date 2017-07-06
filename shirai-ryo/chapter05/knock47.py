from knock41 import Chunk, cabocha_data

for line in cabocha_data():
    for chunk in line:
        verb = ''
        for morph in chunk.get_morphs():
            if morph.get_pos() == '動詞':
                verb = morph.get_base()
        if verb == '':
            continue

        particle_list = list()
        for src in chunk.get_srcs():
            src_morph = line[src].get_word_only_morphs()
            if len(src_morph) > 0 and src_morph[-1].get_pos() =='助詞':
                pair = [src_morph[-1].get_base(), line[src].get_word_only()]
                particle_list.append(pair)
        if len(particle_list) > 0:
            particle, phrase = list(map(list, zip(*sorted(particle_list))))
            if 'を' in particle:
                wo_case = phrase.pop(particle.index('を'))
                particle.pop(particle.index('を'))
                print('{}\t{}\t{}'.format(wo_case + verb, ' '.join(particle), ' '.join(phrase)))
