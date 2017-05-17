from knock41 import Chunk, get_neko_list

for line in get_neko_list():
    for chunk in line:
        dst = chunk.get_dst()
        if chunk.has_noun() is False or dst == -1:
            continue
        answer = list()
        answer.append(chunk.get_word_only())
        
        while dst != -1:
            answer.append(line[dst].get_word_only())
            dst = line[dst].get_dst()
        print(' -> '.join(answer))
