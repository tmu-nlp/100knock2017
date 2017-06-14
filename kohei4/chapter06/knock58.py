"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．
述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）

秋山メモ
目的語、述語の係元の主語の係情報が得られれば、組みとできる。
Element Treeの使い方も、APIマニュアルだけではしんどいので、
素人の言語処理100本ノックを参考に、５２番あたりから勉強。
構造を知るには、正規表現で引っ張ってくるのも良いのだが、５６あたりから
しんどい。
参考WEBでは、便利な、xpath表現の場所指定を使っているが、これでは、
勉強にならないので、使わない形に改編。
あと、デバッグ・解析用に、使う文を指定できるようにした。

"""
# coding: utf-8
#from collections import defaultdict

import re
import xml.etree.ElementTree as ET
import pydot

xml_root = ET.parse('nlp.txt.xml')



beg = 1
end = 100



for sentence in xml_root.iterfind('./document/sentences/sentence'):
    #get sentence id
    sent_no = int(sentence.get('id'))
    if (sent_no >= beg) and (sent_no <= end):

        dict_pred = dict()
        dict_nsubj = dict()
        dict_dobj = dict()

        #for dep in sentence.iterfind(\
        #'./dependencies[@type="collapsed-dependencies"]/dep'):

        for depe in sentence.findall('./dependencies'):
            #print(depe)
            if depe.get('type') == 'collapsed-dependencies':
                #print('yes')
                for dep in depe.findall('dep'):

                    dep_type = dep.get('type')
                    if dep_type == 'nsubj' or dep_type == 'dobj':

                        gover = dep.find('./governor')
                        idx = gover.get('idx')
                        #係元のidx
                        dict_pred[idx] = gover.text
                        #係元の単語
                        if dep_type == 'nsubj':
                            dict_nsubj[idx] = dep.find('./dependent').text
                        else:
                            dict_dobj[idx] = dep.find('./dependent').text

                for idx, pred in sorted(dict_pred.items(),key=lambda x: x[0]):
                    nsubj = dict_nsubj.get(idx)
                    dobj = dict_dobj.get(idx)
                    if (nsubj is not None) and (dobj is not None):
                        print('{}\t{}\t{}'.format(nsubj, pred, dobj))





'''
for token in xml_root.iterfind(\
'./document/sentences/sentence/tokens/token[NER="PERSON"]'\
):
    print(token.findtext('word'))
'''
