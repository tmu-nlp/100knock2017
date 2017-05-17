from knock41 import Chunk, get_neko_list
from graphviz import Digraph

graph = Digraph(format='png')
graph.attr('node', shape='circle')

for line in get_neko_list(5):
    for chunk in line:
        origin = chunk.get_string()
        destination = line[chunk.get_dst()].get_string()
        graph.node(origin)
        if chunk.get_dst() != -1:
            graph.edge(origin, destination)

print(graph)
graph.render('knock44_result')
