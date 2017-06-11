"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
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
        l = re.search(r'<lemma>(.*?)</lemma>',line)
        if l:
            lemma = l.group(1)

        P = re.search(r'<POS>(.*?)</POS>',line)
        if P:
            POS = P.group(1)
            #one_set = [word,lemma,POS]
            print('{}\t{}\t{}'.format(word,lemma,POS))



'''
import xml.etree.ElementTree as ET

xml_root=ET.parse('nlp.txt.xml')

for token_mem in xml_root.iter('token'):
    word = token_mem.findtext('word')
    lemma = token_mem.findtext('lemma')
    pos = token_mem.findtext('POS')

    print('{}\t{}\t{}'.format(word,lemma,pos))
'''
