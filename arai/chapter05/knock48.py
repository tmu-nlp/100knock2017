from knock41 import Chunk, cabocha_data

for line in cabocha_data():
    for chunk in line:
        dst = chunk.dst
        flag = False
        for morph in chunk.morphs:
            if morph.pos == '名詞':
                flag = True
                break
        if flag == False and chunk.dst == -1:
            continue
        answer = []
        answer.append(chunk.get_word_only())

        while dst != -1:
            answer.append(line[dst].get_word_only())
            dst = line[dst].dst
        print(' -> '.join(answer))


