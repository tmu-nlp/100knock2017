'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
'''
from get_chunks_list import get_chunks_list

sents_list = get_chunks_list()
for chunklist in sents_list:#sents_listの要素は、一文のチャンクリスト
    # target_chunk = chunklist.copy()
    for c in chunklist: #ある一文のチャンクをすべてチェックする
        if c.link < 0: #文の終端のチャンクのかかり先はないので-1
            break
        for cc in sents_list[c.sentence_id]:
            if c.link == cc.cid and c.has_noun and cc.has_verb:
                src_sent = ''
                dest_sent = ''
                for srcs in c.morphs:
                    src_sent += srcs.token_body_exclude_symbol
                    # src_sent += srcs.solve_knock40['surface'] + ' '
                for dest in cc.morphs:
                    dest_sent += dest.token_body_exclude_symbol
                    # dest_sent += dest.solve_knock40['surface'] + ' '
                print("{}\t{}".format(src_sent, dest_sent))
