''' 
Ans. for knock45
45. 動詞の格パターンの抽出
'''

from get_chunks_list import get_chunks_list

sents_list = get_chunks_list()
for sent in sents_list:#sentはchunkのリスト(つまり文)
    target_sent = sent.copy()
    for c in sent:
        if c.has_verb:
            verb_base, verb_cid, verb_sid = c.first_verb
            pp = []
            for cc in target_sent:
                if verb_cid > cc.cid and verb_cid == cc.link:
                    for m in cc.morphs:
                        if m.token_pos == '助詞':
                            pp.append(m.features['surface'])
            if len(pp) > 0:
                pp.sort()
                print(str(verb_sid) + ' : ' + verb_base +'\t' + '\t'.join(pp))
            # for debug
            # if verb_sid == 10:
            #     import sys
            #     sys.exit(0)
