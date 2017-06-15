import xml.etree.ElementTree as et

with open('../data/nlp.txt.xml') as i_f,open('answer55.txt','w') as a_f:
    par = et.parse(i_f)
    for xml in par.iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]'):
        word = xml.findtext('word')
        a_f.write('{}\n'.format(word))
