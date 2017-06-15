import xml.etree.ElementTree as ET
import pydot

def make_corenlp_tree(data_in_path, data_out_path, num_sentence):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    i = 0
    for dependencies in root.findall(".//dependencies"):
        if dependencies.get('type') != 'collapsed-dependencies':
            continue
        i += 1
        if i != num_sentence:
            continue
        graph = pydot.Dot()
        graph.set_type('digraph')
        for dep in dependencies.findall('dep'):
            from_edge = dep.find('governor').text + ' _ ' + dep.find('governor').get('idx')
            to_edge = dep.find('dependent').text + ' _ ' + dep.find('dependent').get('idx')
            if to_edge in ',':
                to_edge = r'\,'
            graph.add_edge(pydot.Edge(from_edge, to_edge))
        graph.write_jpeg(data_out_path)
        break

if __name__ == '__main__':
    data_in_path = '../data/knock50_result.txt.xml'
    data_out_path = 'knock57_result.jpg'
    make_corenlp_tree(data_in_path, data_out_path, 4)
