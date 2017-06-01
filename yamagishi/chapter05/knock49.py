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
        i_path = search_path(line, i, -1)
        if len(i_path) == 0 or line[i].has_noun() is False:
            continue

        for j in range(i + 1, length):
            j_path = search_path(line, j, -1)
            if len(j_path) == 0 or line[j].has_noun() is False:
                continue
            
            answer = list()

            # 以下が成り立つとき、j_pathはi_pathに内包される
            if len(i_path) == len(set(i_path + j_path)):
                j_dst = line[i].get_dst()
                for count, dst in enumerate(search_path(line, i, j_path[0])):
                    answer.append(line[dst].get_word_only() if count > 0 else line[dst].get_change_char('X'))
                # 最後にappendした文節はjなので、jに含まれる名詞をYに変えるための処理をする
                answer.pop()
                answer.append(line[dst].get_change_char('Y'))
                print(' -> '.join(answer))

            # そうでないとき、文節iと文節jはある地点kで合流するため、|で繋ぐ必要がある
            else:
                # i_pathにあってj_pathにないもの
                x = list()
                for count, i_dst in enumerate(sorted(list(set(i_path) - set(j_path)))):
                    x.append(line[i_dst].get_word_only() if count > 0 else line[i_dst].get_change_char('X'))
                answer.append(' -> '.join(x))
                
                # j_pathにあってi_pathにないもの
                y = list()
                for count, j_dst in enumerate(sorted(list(set(j_path) - set(i_path)))):
                    y.append(line[j_dst].get_word_only() if count > 0 else line[j_dst].get_change_char('Y'))
                answer.append(' -> '.join(y))

                # i_pathとj_pathの共通部分が、合流後からのpath
                # 欲しい文節は、合流点k
                # k_dstには-1(root)と合流点kからのpathが入るので、2番目のdstが合流点kを示す
                k_dst = sorted(list(set(i_path) & set(j_path)))
                answer.append(line[k_dst[1]].get_word_only())

                print(' | '.join(answer))
