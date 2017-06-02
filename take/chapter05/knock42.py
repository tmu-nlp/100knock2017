'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
'''
from get_chunks_list import get_chunks_list

sents_list = get_chunks_list()
for chunklist in sents_list:#sents_listの要素は、一文のチャンクリスト
    # target_chunk = chunklist.copy()
    for c in chunklist: #ある一文のチャンクをすべてチェックする
        if c.link < 0: #文の終端のチャンクのかかり先はないので-1
            break
        for cc in sents_list[c.sentence_id]:
            if c.link == cc.cid:
                src_sent = ''
                dest_sent = ''
                for srcs in c.morphs:
                    src_sent += srcs.token_body_exclude_symbol
                    # src_sent += srcs.solve_knock40['surface'] + ' '
                for dest in cc.morphs:
                    dest_sent += dest.token_body_exclude_symbol
                    # dest_sent += dest.solve_knock40['surface'] + ' '
                print("{}\t{}".format(src_sent, dest_sent))
