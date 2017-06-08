import pydot
from bs4 import BeautifulSoup, element
'''
<dep type="root">
            <governor idx="0">ROOT</governor>
            <dependent idx="3">claimed</dependent>
          </dep>
'''
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")
dependencies = soup.find_all('dependencies',{"type" : "collapsed-dependencies"})
graph = pydot.Dot('"class dependency"',graph_type='digraph',strict='true')# strick for 重複ノードを削除
for dependence in dependencies:
    for child in dependence.children:
        governor = child.find("governor")
        if isinstance(governor,element.Tag):
            src = governor.text.strip("\n")
            dst = child.find("dependent").text.strip("\n")
            src = '"{}"'.format(src)#prevent error　from not record it as str, so need to double-quote 
            dst = '"{}"'.format(dst)
            node_src = pydot.Node(src)
            node_dst = pydot.Node(dst)
            graph.add_node(node_src)
            graph.add_node(node_dst)
            #どっちかわかんないけど、頭かしっぽいか・・・とりあえず
            graph.add_edge(pydot.Edge(node_src, node_dst,label= '"{}"'.format(child['type'])))
            #graph.add_edge(pydot.Edge(node_dst, node_src,label= '"{}"'.format(child['type'])))
    
    break#一枚だけ作ればいいじゃ無い？
graph.write_png('graph57.png')
