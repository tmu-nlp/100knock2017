from get_chunks_list import get_chunks_list
from itertools import combinations

def get_root(_chunks_list, _chunk):
    if _chunk.is_root():
        return list([_chunk])
    else:
        next_chunk = _chunk.link
        return [_chunk] + get_root(_chunks_list, _chunks_list[next_chunk])

def morphs_formatter(_chunks):
    mor_list = [c.allbody_exc_symbol_as_list for c in _chunks]
    return ' -> '.join(mor_list)

# get_chunks_list()の戻りは, sentence (Chunk型のリスト) のリスト
# 空行を無視し0オリジンなので、sentence[5]が例文（8文目）に相当
for sent in get_chunks_list()[0:7]:
    np_chunk_list = [c for c in sent if c.has_noun]
    all_np_pair_list = list(combinations(np_chunk_list, 2))

    if len(all_np_pair_list) == 0:
        continue

    #名詞句ペアを総当りで調べる
    for np_pair in all_np_pair_list:
        chunk_i, chunk_j = np_pair

        # 題意より i < j なので除外
        if not chunk_i.cid < chunk_j.cid:
            continue

        #iからrootまでのチャンクのリスト
        i_path = get_root(sent, chunk_i)

        #jからrootまでのチャンクのリスト
        j_path = get_root(sent, chunk_j)

        # i,jチャンクの名詞トークンをX,Yで置換
        chunk_i.substitute_to('X')
        chunk_j.substitute_to('Y')

        if set(j_path).issubset(set(i_path)): #ipathにjpathが包含されるとき
            j_on_i = i_path.index(chunk_j) #i上のjチャンクのインデックス
            print(morphs_formatter(i_path[0: j_on_i + 1]))#i-pathをチャンクjまで->で連結表示

        else:
            i_j = list(set(i_path) - set(j_path))
            j_i = list(set(j_path) - set(i_path))
            both_ij = list(set(j_path) & set(i_path))

            i_j.sort(key=lambda x: x.cid)
            j_i.sort(key=lambda x: x.cid)
            both_ij.sort(key=lambda x: x.cid)

            ijk_result = []
            if len(i_j) >0:
                ijk_result.append(morphs_formatter(i_j))

            if len(j_i) >0:
                ijk_result.append(morphs_formatter(j_i))

            if len(both_ij) >0:
                ijk_result.append(morphs_formatter(both_ij))

            print(' | '.join(ijk_result))

        #置換した名詞トークンを戻す
        chunk_i.revert_subX()
        chunk_j.revert_subX()
