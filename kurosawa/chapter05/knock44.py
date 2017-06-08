import pydot
from knock41 import make_chank

def make_str(morph_use):
    str_make = ''
    for morph_print in morph_use.get_morphs():
        if morph_print.get_pos() != '記号':
            str_make += morph_print.get_surface()
    return str_make

if __name__ == '__main__':
    edges = []
    s = int(input('何行目の係り受け木を出力しますか >>'))
    for i,line_main in enumerate(make_chank()):
        if i == s-1:
            lines_main = []
            for j in range(len(line_main)):
                lines_main.append(line_main[j])
            for k in range(j):
                dst_print = int(lines_main[k].get_dst())
                if dst_print != -1:
                    str1 = make_str(lines_main[k])
                    str2 = make_str(lines_main[dst_print])
                    edges.append((str2,str1))
    graph = pydot.graph_from_edges(edges, directed=True)
    graph.write_png('graph.png')
    print('出力しました(graph.png)')
