from knock41 import Chunk, cabocha_data
from graphviz import Digraph



for j,line in enumerate(cabocha_data()):
    G = Digraph(format = 'png')
    G.attr('node', shape = 'circle')
    for i,chunk in enumerate(line):
        G.node(str(i),chunk.get_word_only())
    for i,chunk in enumerate(line):
        if chunk.dst != -1:
            G.edge(str(i) , str(chunk.dst))


    G.render('binary_tree{}'.format(str(i)))
    if j == 3:
        break
