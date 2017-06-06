from knock41 import get_neko_list, Chunk

for line in get_neko_list():
    for chunk in line:
        if chunk.has_noun() is False:
            continue
        dst = chunk.get_dst()
        if dst != -1 and line[dst].has_verb():
            origin = chunk.get_word_only()
            destination = line[dst].get_word_only()
            if len(origin) > 0 and len(destination) > 0:
                print('{}\t{}'.format(origin, destination))


