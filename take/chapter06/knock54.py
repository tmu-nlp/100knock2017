from xml.etree.ElementTree import *

def dump(node):
    for c in node:
        if c.tag == "token":
            for i in c:
                if i.tag == 'word' or i.tag == 'lemma':
                    print(i.text+'\t', end='')
                elif i.tag == 'POS':
                    print(i.text, end='')
            print('')
        dump(c)

tree = parse("nlp.txt.xml")
root = tree.getroot()
dump(root)
