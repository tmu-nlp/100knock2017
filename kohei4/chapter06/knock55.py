"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ
"""
# coding: utf-8
#from collections import defaultdict

import re

one_set = []
token_list = []
with open('nlp.txt.xml', 'r') as fxml:
    for line in fxml:
        w = re.search(r'<word>(.*?)</word>',line)
        if w:
            word = w.group(1)
        N = re.search(r'<NER>(.*?)</NER>',line)
        if N and N.group(1) == 'PERSON':
            print(word)



'''
import xml.etree.ElementTree as ET

xml_root=ET.parse('nlp.txt.xml')

for token in xml_root.iterfind(/
'./document/sentences/sentence/tokens/token[NER="PERSON"]'/
):
    print(token.findtext('word'))

'''
