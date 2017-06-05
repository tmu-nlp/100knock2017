from get_chunks_list import get_chunks_list

sents_list = get_chunks_list()
#空行をのぞいているため、元ファイルの7行目に相当する
for c in sents_list[3+1]: # 0オリジンのため１足す
    for m in c.morphs:
        print(m.feature)
