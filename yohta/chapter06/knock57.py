# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい
import xml.etree.ElementTree as et
import pydot_ng as pd

def graph_write(edgelist):
    graph = pd.Dot(graph_type = 'digraph')

    for edge in edgelist:
        bef_num = str(edge[0][0])
        aft_num = str(edge[1][0])
        bef_word = str(edge[0][1])
        aft_word = str(edge[1][1])

        graph.add_node(pd.Node(bef_num,label = bef_word))
        graph.add_node(pd.Node(aft_num,label = aft_word))

        graph.add_edge(pd.Edge(bef_num,aft_num))

    return graph

with open('../data/nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    for sentence in par.iterfind('./document/sentences/sentence'):
        sent_id = int(sentence.get('id'))       # sentenceのid

        edge = []
        for depend in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            # punct = 句読点
            if depend.get('type') != 'punct':
            # governor、dependent取得、edgeに追加
                gov = depend.find('./governor')
                dep = depend.find('./dependent')
                if gov.text != 'ROOT':
                    edge.append(((gov.get('idx'), gov.text), (dep.get('idx'), dep.text)))
    # 描画
        if len(edge) > 0:
            graph = graph_write(edge)
            graph.write_png('answer57/answer57_{}.png'.format(sent_id))
