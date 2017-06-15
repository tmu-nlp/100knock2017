from graphviz import Digraph
import pydot_ng as pydot
from knock41 import func41, Chunk

"""
edges = [(1,2),(1,3),(1,4),(3,4)]
g = pydot.graph_from_edges(edges)
g.write_jpeg('graph_from_edges_dot.jpg',prog = 'dot')
"""
"""
b(class Chunk) in line下で
掛かり先のChunkの表層形：ingword = b.getSurword()
掛かり元のChunkの表層形：edword = line[b.getDst()].getSurword()

Digraph:有向グラフ
Graph:無向グラフ
"""

g = Digraph(format='png')
g.attr('node',shape = 'circle')

N = 15
counter = 0
#for line in range(N):
for line in func41():
    if counter > N:
        break
    for b in line:
        ingword = b.getSurword()
        edword = line[b.getDst()].getSurword()
        if len(ingword) > 0 and len(edword) > 0:
            if b.getDst() != -1:
                g.edge(ingword,edword)

#    print(g)

    g.render('tree_neko')
    counter += 1
"""
from graphviz import Digraph

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')

N = 15    # ノード数

# ノードの追加
for i in range(N):
    G.node(str(i), str(i))

# 辺の追加
for i in range(N):
    if (i - 1) // 2 >= 0:
        G.edge(str((i - 1) // 2), str(i))

# print()するとdot形式で出力される
print(G)

# binary_tree.pngで保存
G.render('binary_tree')
"""
