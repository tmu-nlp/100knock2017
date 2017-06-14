from knock41 import Chunk, cabocha_data

for line in cabocha_data():
    for chunk in line:
        for morph in chunk.morphs:
            if morph.pos == "名詞":
                dst = chunk.get_dst()
                if dst != -1 and "動詞" in [morph.get_pos() for morph in line[dst].get_morphs()]:
                    origin = chunk.get_word_only()
                    destination = line[dst].get_word_only()
                    if len(origin) > 0 and len(destination) > 0:
                        print(origin + "\t" + destination)
                        # print('{}\t{}'.format(origin, destination))
