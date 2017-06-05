import pydot
from knock41 import make_chunk_list

line_number = int(input('何行目の依存構造木が欲しいですか : '))

chunk_list = make_chunk_list()
edges = list()
phrase_dict = dict()
for i,word in enumerate(chunk_list[line_number]):
    morphs = word.getMorphs()
    temp_str = ''
    for morph in morphs:
        temp_str += morph.getSurface()
    phrase_dict[i] = temp_str    

for i, word in enumerate(chunk_list[line_number]):
    morphs = word.getMorphs()
    dst = int(word.getDst())
    if dst == -1:
        continue
    edges.append((phrase_dict[dst], phrase_dict[i]))    
    #edges.append((phrase_dict[i], phrase_dict[dst]))

g=pydot.graph_from_edges(edges,'',True)
g.write_jpeg('graph_from_edges_dot.jpg', prog='dot')
