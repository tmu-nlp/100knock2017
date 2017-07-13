from knock41 import Chunk, cabocha_data


def path(i, j):
    head_i, i = i
    head_j, j = j
    last_i, last_j =i[-1],j[-1]
    for c_i, c_j in zip(i[::-1], j[::-1]):
        if c_i == c_j:
            last_i, last_j = c_i, c_j 
            continue
        else:
            break
    i = i[:i.index(last_i)]
    j = j[:j.index(last_j)]
    if len(j) == 0 and len(i) > 0:
        i[0] = i[0].replace(head_i, 'X')
        print('->'.join(i) + '-> Y')
    elif len(i) > 0 and len(j) > 0:
      
        i[0] = i[0].replace(head_i, 'X')
        j[0] = j[0].replace(head_j, 'Y')
        print('{}|{}|{}'.format('->'.join(i), '->'.join(j), last_i))
n = 0
for line in cabocha_data():
    n += 1
    answers = []
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
        head_noun = morph.surface

        while dst != -1:
            answer.append(line[dst].get_word_only())
            dst = line[dst].dst
        answers.append((head_noun, answer))

    for i in range(len(answers)-1) :
        for j in range(i+1, len(answers)):
                path(answers[i], answers[j])



