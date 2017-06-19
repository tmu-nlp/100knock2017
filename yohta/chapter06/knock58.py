import xml.etree.ElementTree as et

with open('../data/nlp.txt.xml') as i_f,open('answer58.txt','w') as a_f:
    par = et.parse(i_f)
    a_f.write('nsubj\tpred\tdobj\n\n')
    for sentence in par.iterfind('./document/sentences/sentence'):
        sent_id = int(sentence.get('id'))       # sentenceのid
        # それぞれの語の辞書を作成
        dict_pred = {}      # pred_idx, pred_text
        dict_nsubj = {}     # 主語:pred_idx, nsubj_text
        dict_dobj = {}      # 目的語:pred_idx, dobj_text
        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            dep_type = dep.get('type')
            if dep_type == 'nsubj' or dep_type == 'dobj':
                # 述語の辞書
                gov = dep.find('./governor')
                idx = gov.get('idx')
                dict_pred[idx] = gov.text
                # 主語か目的語の辞書
                if dep_type == 'nsubj':
                    dict_nsubj[idx] = dep.find('./dependent').text
                else:
                    dict_dobj[idx] = dep.find('./dependent').text
            # 述語のうち、主語と目的語の両方を持つもののみ出力
        for idx, pred in sorted(dict_pred.items(), key=lambda x: x[0]):
            nsubj = dict_nsubj.get(idx)
            dobj = dict_dobj.get(idx)
            if nsubj != None and dobj != None:
                a_f.write('{}\t{}\t{}\n'.format(nsubj, pred, dobj))
