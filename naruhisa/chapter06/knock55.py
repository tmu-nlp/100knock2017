import xml.etree.ElementTree as et

with open('nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    for token in par.iter('token'):
        ner = token.find('NER').text
        if ner == 'PERSON':
            print('{}' .format(token.find('word').text))
