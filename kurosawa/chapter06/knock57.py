import xml.etree.ElementTree as ET
import pydot
from knock53 import xml_parse

if __name__ == '__main__':
    root = xml_parse('nlp.txt.xml')
    s = int(input('何行目の係り受けを出力しますか >>'))
    for sen in list(root.getiterator('sentence')):
        if sen.get('id') == str(s):
            edges = []
            dep = sen.find('.//dependencies')
            for word_ in list(dep.getiterator('dep')):
                if word_.get('type') != 'punct':
                    edges.append((word_.findtext('governor'),word_.findtext('dependent')))
            graph = pydot.graph_from_edges(edges, directed=True)
            graph.write_png('graph.png')
            print('出力しました(graph.png)')
            break
