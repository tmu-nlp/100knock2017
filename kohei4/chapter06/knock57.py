"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

秋山メモ
係り受けのエッジ情報が得られれば、可視化出来る。
Element Treeの使い方も、APIマニュアルだけではしんどいので、
素人の言語処理100本ノックを参考に、５２あたりから勉強。
構造を知るには、正規表現で引っ張ってくるのも良いのだが、５６あたりから
しんどい。
参考WEBでは、便利な、xpath表現の場所指定を使っているが、これでは、
勉強にならないので、使わない形に改編。
なんとか動作。
可視化の際、ラベル頼りに描くと、同じ単語が出ると縮退してしまうので、
エッジ情報＋ラベルとした。
あと、デバッグ・解析ように、出力文を指定できるようにした。
"""
# coding: utf-8
#from collections import defaultdict

import re
import xml.etree.ElementTree as ET
import pydot

xml_root = ET.parse('nlp.txt.xml')


sentences=[]
beg = 1
end = 4

def graph_from_idx_edges(edges):
    graph = pydot.Dot(graph_type = 'digraph')

    for edge in edges:

        idx1 = str(edge[0][0])
        label1 = str(edge[0][1])
        idx2 = str(edge[1][0])
        label2 = str(edge[1][1])

        graph.add_node(pydot.Node(idx1, label=label1))
        graph.add_node(pydot.Node(idx2, label=label2))

        graph.add_edge(pydot.Edge(idx1, idx2))

    return graph


for sentence in xml_root.iterfind('./document/sentences/sentence'):
    #get sentence id
    sent_no = int(sentence.get('id'))
    if (sent_no >= beg) and (sent_no <= end):

        edges = []

        #not use Xpath
        #for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):

        for depe in sentence.findall('./dependencies'):
            #print(depe)
            if depe.get('type') == 'collapsed-dependencies':
                #print('yes')
                for dep in depe.findall('dep'):
                    if dep.get('type') != 'punct':

                        gover = dep.find('./governor')
                        deped = dep.find('./dependent')
                        edges.append(((gover.get('idx'),gover.text),(deped.get('idx'),deped.text)))
                    #print(edges)

        #sentences.append(edges)

        if len(edges) > 0:

            graph = graph_from_idx_edges(edges)
            graph.write_png('{}.png'.format(sent_no))



"""
for token in xml_root.iterfind(\
'./document/sentences/sentence/tokens/token[NER="PERSON"]'\
):
    print(token.findtext('word'))
"""
