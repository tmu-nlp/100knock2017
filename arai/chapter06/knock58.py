from xml.etree import ElementTree

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)

for j,word in enumerate(tree.iter('dependencies')):
    if word.attrib['type'] == 'collapsed-dependencies':
        nsubj_v = 'gggggggggggggggg'
        obj = 'hhhhhhhhhhhhhhhhhh'
        s ='nnnnnnnnnnnnnnnn'
        dobj_v = 'ooooooooooooo'
        for word_ in word.iter('dep'):
            if word_.attrib['type'] == 'nsubj':
                nsubj_v = word_.findtext('.//governor')
                s = word_.findtext('.//dependent')
            elif word_.attrib['type'] == 'dobj':
                dobj_v = word_.findtext('.//governor')
                obj = word_.findtext('.//dependent')
        if nsubj_v == dobj_v:
            print(s + '\t' + nsubj_v + '\t' + obj)
   
    
