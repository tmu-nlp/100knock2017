from knock41 import Chunk, cabocha_data

for line in cabocha_data():
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
