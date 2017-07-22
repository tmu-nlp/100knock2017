from xml.etree import ElementTree
from nltk.tree import *

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)
for s in tree.iter('parse'):
    tree = ParentedTree.fromstring(s.text)
    sub_trees = list(tree.subtrees())
    for sub_tree in sub_trees:
        if sub_tree.label() == 'NP':
            tokens = list(sub_tree.leaves())
            print(' '.join(tokens))
