from xml.etree import ElementTree

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)
for word in tree.iter('token'):
    print('{}\t{}\t{}'.format(word.findtext('.//word') , word.findtext('.//lemma') , word.findtext('.//POS')))
