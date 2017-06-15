import xml.etree.ElementTree as et

with open('../data/nlp.txt.xml') as i_f,open('answer53.txt','w') as a_f:
    par = et.parse(i_f)
    for word in par.iter('word'):
        a_f.write(word.text + '\n')
