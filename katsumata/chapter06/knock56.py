"""
話の流れ
何も考えず1行ずつ出力する
coreferenceが存在したらそれをreplaceする形
は、なんか嫌なので先に修正リスト(クラスでいいんじゃ,
嘘、辞書で良い)のようなものを作ってそこに
sentence idを投げてもしあったら修正していく(replaceかなぁ)方式に
"""
from xml.etree.ElementTree import *
from collections import defaultdict
tree = parse('nlp.txt.xml')
elem = tree.getroot()

doc = elem.find('document')

sentences = doc.find('sentences')
corefer_dict = defaultdict(int)

coreference = doc.find('coreference')
for child_corefer in coreference.findall('coreference'):
    for mentions in child_corefer.findall('mention'):
        sentence_num = int(mentions.find('sentence').text)
        if mentions.get('representative'):
            origin_mention = mentions.find('text').text 
        else:
            corefer_dict[sentence_num] = (origin_mention, mentions.find('text').text)
"""
sentence単位で文を出力させる
とりあえず文をappend形式で作ってreplace
時間があればtoken_idを用いて動的に表示
"""
for child in sentences.findall('sentence'):
    id_num = int(child.get('id'))
    line = ''
    for words in child.iter('word'):
        line += words.text + ' '
    if corefer_dict[id_num] != 0:
        r_mention, mention = corefer_dict[id_num]
        replace_word = '{}({})'.format(r_mention, mention)
        line = line.replace(mention, replace_word)
    print (line)
    """
    line = ''
    for words in child.iter('word'):
        word = words.text
        if corefer_dict[id_num] != 0:
            word = そのtoken_idの単語
        line += word    
    """

