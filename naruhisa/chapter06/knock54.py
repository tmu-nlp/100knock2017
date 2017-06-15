import xml.etree.ElementTree as et

with open('nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    for token in par.iter('token'):
        word = token.find('word').text
        lemma = token.find('lemma').text
        POS = token.find('POS').text
        print('{}\t{}\t{}' .format(word, lemma, POS))
