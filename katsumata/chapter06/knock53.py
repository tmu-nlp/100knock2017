from xml.etree.ElementTree import *

input_f = 'nlp.txt.xml'

tree = parse(input_f)
elements = tree.getroot()

wordlist = elements.findall('.//word')
for word in wordlist:
    print (word.text)
