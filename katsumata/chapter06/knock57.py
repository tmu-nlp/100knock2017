import pydot
from xml.etree.ElementTree import *

line_number = int(input('何行目の係り受け木が欲しいですか : '))

tree = parse('nlp.txt.xml')
elem = tree.getroot()
doc = elem.find('document')
sentences = doc.find('sentences')
edges = list()

for child_sentence in sentences.findall('sentence'):
    id_num = int(child_sentence.get('id'))
    if id_num != line_number:
        continue
    for depends in child_sentence.findall('dependencies'):
        if depends.get('type') == 'collapsed-dependencies':
            for dep in depends.findall('dep'):
               edges.append((dep.find('governor').text, dep.find('dependent').text)) 
g = pydot.graph_from_edges(edges, '', True)
g.write_jpeg('dependency_graph.jpg', prog='dot')
