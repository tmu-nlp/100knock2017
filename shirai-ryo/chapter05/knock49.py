from knock41 import Chunk, cabocha_data

def search_path(line, chunk_num, goal):
    path = list()
    path.append(chunk_num)
    while path[-1] != goal:
        path.append(line[path[-1]].get_dst())
    return path


for line in cabocha_data():
    length = len(line)
    for i in range(length):
        if line[i].has_noun() is False:
            continue
        i_path = search_path(line, i, -1)

        for j in range(i + 1, length):
            if line[j].has_noun() is False:
                continue
            j_path = search_path(line, j, -1)
            answer = list()
            i_path_set = set(i_path)
            j_path_set = set(j_path)

            if j_path_set.issubset(i_path_set):
                j_dst = line[i].get_dst()
                for count, dst in enumerate(search_path(line, i, j_path[0])):
                    answer.append(line[dst].get_word_only() if count > 0 else line[dst].get_change_char('X'))
                answer.pop()
                answer.append('Y')
                print(' -> '.join(answer))

            else:
                x = list()
                for count, i_dst in enumerate(sorted(i_path_set - j_path_set)):
                    x.append(line[i_dst].get_word_only() if count > 0 else line[i_dst].get_change_char('X'))
                answer.append(' -> '.join(x))

                y = list()
                for count, j_dst in enumerate(sorted(j_path_set - i_path_set)):
                    y.append(line[j_dst].get_word_only() if count > 0 else line[j_dst].get_change_char('Y'))
                answer.append(' -> '.join(y))

                k_path = sorted(i_path_set & j_path_set)
                answer.append(line[k_path[1]].get_word_only())

                print(' | '.join(answer))
