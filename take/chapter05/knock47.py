'''
 Ans. for knock47

 47. 機能動詞構文のマイニング
 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．
 返事をする      と に は        及ばんさと 手紙に 主人は

 このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

 コーパス中で頻出する述語（サ変接続名詞+を+動詞）
 コーパス中で頻出する述語と助詞パターン
'''

from get_chunks_list import get_chunks_list

sents_list = get_chunks_list()
for sent in sents_list:#sentはchunkリスト(文)のリスト
    target_sent = sent.copy()
    for c in sent:
        if c.has_verb:
            verb_base, verb_cid, verb_sid = c.first_verb
            pp = []
            ppbody = []
            sahen = []
            sahen_chunk_id =[]
            for cc in target_sent:
                if verb_cid > cc.cid and verb_cid == cc.link:
                    if len(cc.morphs) == 2:
                        if cc.morphs[0].token_pos1 == 'サ変接続' \
                                and cc.morphs[1].token_pos == '助詞' and cc.morphs[1].token_body == 'を':
                            sahen.append(cc.morphs[0].token_body + 'を' + verb_base)
                            sahen_chunk_id.append(cc.cid)
                    for m in cc.morphs:#かかり先述語までの各チャンクを構成するmorphを走査する。
                        if cc.cid in sahen_chunk_id:
                            break
                        if m.token_pos == '助詞':
                            pp.append(m.features['surface'])
                            ppbody.append(cc.allbody)
                    # if verb_sid == 868 and len(pp) > 0 and len(sahen_chunk_id) > 0:
                    if len(pp) > 0 and len(sahen_chunk_id) > 0:
                        pp.sort()
                        ppbody_ = list(set(ppbody)) #述語を指すチャンクに複数助詞がある場合重複するので。我ながらgomiコードすぎて死ねる
                        print(str(verb_sid) + ' : ' + ''.join(sahen) +'\t' + '\t'.join(pp) +'\t' + '\t'.join(ppbody_))
