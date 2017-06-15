"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．

秋山メモ
この手の処理には、左括弧ー右括弧をカウンターで数え流という
プロトコルが一般的らしいので、XMLのparseセクションにある、
S式をそれで解析。
ただ、初めてのアルゴリズムなので、参考にした素人の言語処理100本ノックさん
のコードを超えるものを思いつかなく、写経になった。
安全策（re.DOTALL strip等チェック)
ElementTreeの使い方も標準的なもので良く、センテンスIDを直接取りにくいので、
enumerateを使い、デバック・解析用に、使う文書を指定できるようにした。
S式で、直接、括弧を数えるという方法も考えたし、作例もみたが、複雑になって
しまい、見通しが悪いので、再帰関数方式が良いが、それでも複雑。



"""
# coding: utf-8
#from collections import defaultdict

import re
import xml.etree.ElementTree as ET
import pydot

#pattern = re.compile(r'^\((.*?)\s(.*)\)$',re.DOTALL)
#re.DOTALL no need for corenlp-full-2016-10-31
pattern = re.compile(r'^\((.*?)\s(.*)\)$')
xml_root = ET.parse('nlp.txt.xml')

beg = 1
end = 2

def NP_Parse(str, list_np):
    match = pattern.match(str)
    #正規表現で（一皮）むく
    tag = match.group(1)
    value = match.group(2)
    #print(tag)
    #print(value)
    #print(list_np)
    #These debug print is good to check the recursive func.

    depth = 0
    chunk = ''
    words = []
    for c in value:
        #print(c)
        #一皮剥いた中身を一つずつチェック
        #chunkに積み直し
        if c == '(':
            chunk += c
            depth += 1
            #（で一つ深く
        elif c == ')':
            chunk += c
            depth -= 1
            #　)で一つ浅く、０で外にでたら、剥いた中身をRecursiveにチェック
            if depth == 0:
                #print(chunk,list_np)
                words.append(NP_Parse(chunk,list_np))
                chunk = ''

        else:
            if not (depth == 0 and c== ' '):
                #print('here1')
                chunk += c
                #その他空白以外は積んでいく

    if chunk != '':
        #Add the Remained word
        words.append(chunk)
        #print(chunk)
    result = ' '.join(words)
    #print('result='+result)
    if tag == 'NP':
        list_np.append(result)
    return result

for ii, parse in enumerate\
( xml_root.iterfind('./document/sentences/sentence/parse')):
    #get sentence id
    if (ii+1 >= beg) and (ii+1 <= end):
    #print(ii)
        parse_str = parse.text
        #.text Element Object attribute
        result = []
        #print(parse_str)
        #print(parse_str.strip())
        NP_Parse(parse_str.strip(),result)
        # No needs for strip() for this version of NLP core.
        print(*result, sep = '\n')
