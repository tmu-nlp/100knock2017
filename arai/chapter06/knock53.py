from xml.etree import ElementTree 

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)
for word in tree.iter('word'):
    print(word.text)


