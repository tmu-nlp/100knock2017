from knock41 import get_neko_list, Chunk

for line in get_neko_list():
    for chunk in line:
        dst = chunk.get_dst()
        if dst != -1 and '動詞' in [morph.get_pos() for morph in line[dst].get_morphs()]:
            origin = chunk.get_word_only()
            destination = line[dst].get_word_only()
            if len(origin) > 0 and len(destination) > 0:
                print('{}\t{}'.format(origin, destination))


