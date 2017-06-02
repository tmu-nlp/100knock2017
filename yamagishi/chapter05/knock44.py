from knock41 import Chunk, get_neko_list
from graphviz import Digraph

for i, line in enumerate(get_neko_list()):
    if i > 5:
        break
    
    graph = Digraph(format='png')
    graph.attr('node', shape='circle')
    
    for chunk in line:
        origin = chunk.get_string()
        destination = line[chunk.get_dst()].get_string()
        graph.node(origin)
        if chunk.get_dst() != -1:
            graph.edge(origin, destination)

    graph.render('knock44_graph{}'.format(i))
