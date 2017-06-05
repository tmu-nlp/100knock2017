''' 
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを

'''

from get_chunks_list import get_chunks_list

sents_list = get_chunks_list()
for sent in sents_list:#sentはchunkのリスト(つまり文)
    target_sent = sent.copy()
    for c in sent:
        if c.has_verb:
            verb_base, verb_cid, verb_sid = c.first_verb
            pp = []
            ppbody = []
            for cc in target_sent:
                if verb_cid > cc.cid and verb_cid == cc.link:
                    for m in cc.morphs:
                        if m.token_pos == '助詞':
                            pp.append(m.features['surface'])
                    ppbody.append(cc.allbody)
            if len(pp) > 0:
                pp.sort()
                print(str(verb_sid) + ' : ' + verb_base +'\t' + '\t'.join(pp) +'\t' + '\t'.join(ppbody))
            # for debug
            # if verb_sid == 10:
            #     import sys
            #     sys.exit(0)
