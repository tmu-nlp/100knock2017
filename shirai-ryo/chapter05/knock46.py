from knock41 import Chunk, cabocha_data

for line in cabocha_data():
    for chunk in line:
        verb = "" #動詞を入れる
        for morph in chunk.get_morphs():
            if morph.get_pos() == "動詞":
                verb = morph.get_base()
        if verb == "":
            continue

        particle_list = [] #助詞を入れる
        for src in chunk.get_srcs():
            src_morph = line[src].get_morphs()
            if len(src_morph) > 0 and src_morph[-1].get_pos() == "助詞":
                pair = [src_morph[-1].get_base(), line[src].get_word_only()]
                particle_list.append(pair)

            if len(particle_list) > 0:
                particle, phrase = list(zip(*sorted(particle_list)))
                #期待する引数が不定の時には * をつける
                print('{}\t{}\t{}'.format(verb, ' '.join(particle), ' '.join(phrase)))
