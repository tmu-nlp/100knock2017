"""
方針
各単語の<NER>に'PERSON'と入っている<word>を抜き出すっぽい
上から順に操作していく、和集合を求めていけばいいんでないか

"""
from xml.etree.ElementTree import *
input_f = 'nlp.txt.xml'

tree = parse(input_f)
elements = tree.getroot()

wordlist = elements.findall('.//word')
nerlist = elements.findall('.//NER')
for word, ner in zip(wordlist, nerlist):
    if ner.text == 'PERSON':
        print (word.text)
