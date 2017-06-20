from xml.etree import ElementTree

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)
for word in tree.iter('token'):
    if word.findtext('.//NER') == 'PERSON':
        print(word.findtext('.//word'))
