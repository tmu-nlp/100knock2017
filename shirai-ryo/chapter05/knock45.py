from knock41 import Chunk, cabocha_data

for line in cabocha_data():
    for chunk in line:
        verb = "" #動詞を入れる
        for morph in chunk.get_morphs():
            if morph.get_pos() == "動詞":
                verb = morph.get_base()
        if verb == "":
            continue

        particles = list() #助詞を入れる
        for src in chunk.get_srcs():
            src_morph = line[src].get_morphs() #line[変数]のmorphを取ってくる
            if src_morph[-1].get_pos1() == "格助詞":
                particles.append(src_morph[-1].get_base())
        if len(particles) > 0:
            print("{}\t{}".format(verb, " ".join(sorted(particles))))
