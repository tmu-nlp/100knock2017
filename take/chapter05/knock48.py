'''
Ans. for knock48
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''

from get_chunks_list import get_chunks_list

def get_root(chunklist, start_chunk, result_lst):
    res = result_lst
    if start_chunk.link == -1:# or not start_chunk.has_noun:
        return
    if start_chunk.has_noun and len(result_lst) == 0:
        res = [start_chunk.allbody]
    elif start_chunk.has_noun and len(result_lst) > 0:
        res = result_lst
    else:
        pass
    for c in chunklist:
        if start_chunk.cid < c.cid and start_chunk.link == c.cid:
            # print('sid:{} ; link:{} : cid:{}'.format(c.sentence_id, start_chunk.cid, c.cid))
            res.append(c.allbody)
            # print('-----------',res)
            if c.link == -1:
                print(''.join(res))
            else:
                get_root(chunklist, c, res)

sents_list = get_chunks_list()
for sent in sents_list: # sentはchunkリスト(文)のリスト
    target_sent = sent.copy()
    for c in sent:
        if c.has_noun:
            get_root(target_sent, c, [])
    if c.sentence_id > 5:
        break
