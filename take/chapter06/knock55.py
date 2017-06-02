from xml.etree.ElementTree import *

def dump(node):
    for c in node:
        if c.tag == "token":
            for i in c:
                if i.tag == 'word':
                    who = i.text
                if i.tag == 'NER' and i.text == 'PERSON':
                    print(who);who=''
        dump(c)

tree = parse("nlp.txt.xml")
root = tree.getroot()
dump(root)
