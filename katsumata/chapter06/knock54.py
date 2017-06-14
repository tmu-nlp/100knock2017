from xml.etree.ElementTree import *

input_f = 'nlp.txt.xml'

tree = parse(input_f)
elements = tree.getroot()

wordlist = elements.findall('.//word')
poslist = elements.findall('.//POS')
lemmalist = elements.findall('.//lemma')

for word, lemma, pos in zip(wordlist, lemmalist, poslist):
    print ('{}\t{}\t{}'.format(word.text, lemma.text, pos.text))
