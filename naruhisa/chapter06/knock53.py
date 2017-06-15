import xml.etree.ElementTree as et

with open('nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    for word in par.iter('word'):
        print(word.text)
