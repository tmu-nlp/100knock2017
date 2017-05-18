from knock41 import get_neko_list, Chunk

for line in get_neko_list():
    for chunk in line:
        if chunk.get_dst() != -1:
            origin = chunk.get_word_only()
            destination = line[chunk.get_dst()].get_word_only()
            if len(origin) > 0 and len(destination) > 0:
                print('{}\t{}'.format(origin, destination))


