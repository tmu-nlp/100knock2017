"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

java -cp "/usr/local/lib/stanford-corenlp-full-2013-06-20/*"
 -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
 -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt
"""
# coding: utf-8
#from collections import defaultdict
import re


with open('nlp.txt.xml', 'r') as fxml:
    for line in fxml:
        m = re.search(r'<word>(.*?)</word>',line)
        if m:
            print(m.group(1))




'''
import xml.etree.ElementTree as ET

xml_root=ET.parse('nlp.txt.xml')

for word in xml_root.iter('word'):

    print(word.text)

'''
