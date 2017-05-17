from knock41 import Chunk, get_neko_list

def search_path(line, chunk_num, goal):
    path = list()
    path.append(chunk_num)
    while path[-1] != goal:
        path.append(line[path[-1]].get_dst()) 
    return path


for line in get_neko_list():
    length = len(line)
    for i in range(length):
        x_path = search_path(line, i, -1)
        if len(x_path) == 0 or line[i].has_noun() is False:
            continue

        for j in range(i + 1, length):
            y_path = search_path(line, j, -1)
            if len(y_path) == 0 or line[j].has_noun() is False:
                continue
            
            answer = list()
            merge_path = list(set(x_path + y_path))

            # 以下が成り立つとき、yはxに内包される
            if len(x_path) == len(merge_path):
                y_dst = line[i].get_dst()
                for count, dst in enumerate(search_path(line, i, y_path[0])):
                    answer.append(line[dst].get_word_only() if count > 0 else line[dst].get_change_char('X'))
                answer.pop()
                answer.append(line[dst].get_change_char('Y'))
                print(' -> '.join(answer))

            # そうでないとき、文節xと文節yはある地点で合流するため、|で繋ぐ必要がある
            else:
                # xにあってyにないもの
                x = list()
                for count, x_dst in enumerate(sorted(list(set(x_path) - set(y_path)))):
                    x.append(line[x_dst].get_word_only() if count > 0 else line[x_dst].get_change_char('X'))
                answer.append(' -> '.join(x))
                
                # yにあってxにないもの
                y = list()
                for count, y_dst in enumerate(sorted(list(set(y_path) - set(x_path)))):
                    y.append(line[y_dst].get_word_only() if count > 0 else line[y_dst].get_change_char('Y'))
                answer.append(' -> '.join(y))

                # 両方にあるもの (合流してから、yのパスが終わるまで)
                xy = list()
                for xy_dst in sorted(list(set(x_path) & set(y_path))):
                    xy.append(line[xy_dst].get_word_only())
                # 最後の-1がappendされてしまっているので、一つpopする
                xy.pop()
                answer.append(' -> '.join(xy))

                print(' | '.join(answer))
