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
                # 本当は下の方が正しいと思うけど、例が変なので……
                ## 最後にappendした文節はjなので、jに含まれる名詞をYに変えるための処理をする
                #answer.append(line[dst].get_change_char('Y'))
                print(' -> '.join(answer))

            # そうでないとき、文節iと文節jはある地点kで合流するため、|で繋ぐ必要がある
            else:
                # i_pathにあってj_pathにないもの
                x = list()
                for count, i_dst in enumerate(sorted(i_path_set - j_path_set)):
                    x.append(line[i_dst].get_word_only() if count > 0 else line[i_dst].get_change_char('X'))
                answer.append(' -> '.join(x))
                
                # j_pathにあってi_pathにないもの
                y = list()
                for count, j_dst in enumerate(sorted(j_path_set - i_path_set)):
                    y.append(line[j_dst].get_word_only() if count > 0 else line[j_dst].get_change_char('Y'))
                answer.append(' -> '.join(y))

                # i_pathとj_pathの共通部分が、合流後からのpath
                # 欲しい文節は、合流点k
                # k_pathには-1(root)と合流点kからのpathが入るので、2番目のdstが合流点kを示す
                k_path = sorted(i_path_set & j_path_set)
                answer.append(line[k_path[1]].get_word_only())

                print(' | '.join(answer))
