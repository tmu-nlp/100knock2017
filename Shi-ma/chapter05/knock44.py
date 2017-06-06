from knock41 import Chunk, cabocha_chunk_data
import pydot

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        num_line = 6
        graph = pydot.Dot()
        graph.set_type('digraph')
        for i, line in enumerate(cabocha_chunk_data(data_in)):
            if i == num_line:
                break
            for phrase in line:
                from_edge = phrase.get_phrase_txt(); to_edge = line[phrase.dst].get_phrase_txt();
                if from_edge == '' or to_edge == '':
                    continue
                graph.add_node(pydot.Node(from_edge))
                if phrase.dst != -1:
                    graph.add_edge(pydot.Edge(from_edge, to_edge))
        graph.write_jpeg('knock44_result.jpg')
