from xml.etree import ElementTree
from graphviz import Digraph

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)

for j,word in enumerate(tree.iter('dependencies')):
    #print(word.text)
    G = Digraph(format = 'png')
    G.attr('node', shape = 'circle')
    if word.attrib['type'] == 'collapsed-dependencies':
        #print(word.text)
        for word_ in word.iter('dep'):
            dep_ID = word_.find('dependent').attrib['idx']
            dep = word_.findtext('.//dependent')
            G.node(dep_ID, dep)
        #for k, word_ in enumerate(word.iter('dep')):
            gov_ID = word_.find('governor').attrib['idx']
            gov = word_.findtext('.//governor')
            G.node(gov_ID, gov)

            G.edge(dep_ID, gov_ID)


        G.render('binary_tree_{}'.format(str(j)))
        if j == 3:
            break
    
