import pydot
from knock41 import Cabocha
def pair_chunk(chunks):
    result = []
    for chunk in chunks:
        dst = chunk.dst
        if dst == -1:# skip
            continue
        base_morph = chunk.print_morphs()
        dst_morph = chunks[dst].print_morphs()
        result.append((base_morph, dst_morph))
    return result
graph = pydot.Dot(graph_type='digraph')
if __name__ == "__main__":
    for s in Cabocha().get_sentence():
        pair = pair_chunk(s)
        for p in pair:
            node_src = pydot.Node(p[0])
            node_dst = pydot.Node(p[1])
            graph.add_edge(pydot.Edge(node_src, node_dst))
graph.write_png('graph.png')
