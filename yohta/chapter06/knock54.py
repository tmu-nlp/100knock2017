import xml.etree.ElementTree as et

with open('../data/nlp.txt.xml') as i_f,open('answer54.txt','w') as a_f:
    par = et.parse(i_f)
    for xml in par.iter('token'):
        word = xml.findtext('word')
        lem = xml.findtext('lemma')
        pos = xml.findtext('POS')
        a_f.write('{}\t\t{}\t\t{}\n'.format(word,lem,pos))
