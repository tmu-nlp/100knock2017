"""
話の流れ
coreferenceを読み込む
1行ずつ出力する
読み込んだcoreferenceが存在したら処理を行う
sentence idを投げてもしあったら修正していく方式に
"""
class Corefer:
    def __init__(self, pair, start, end):
        self.pair = pair
        self.start = start
        self.end = end
    
    def getPair(self):
        return self.pair
    def getS_E(self):
        return (self.start, self.end)
    def getReplace_w(self):
        return '{0[0]}({0[1]}) '.format(self.pair)


from xml.etree.ElementTree import *
from collections import defaultdict
tree = parse('nlp.txt.xml')
elem = tree.getroot()

doc = elem.find('document')

sentences = doc.find('sentences')
corefer_dict = defaultdict(list)

coreference = doc.find('coreference')
for child_corefer in coreference.findall('coreference'):
    for mentions in child_corefer.findall('mention'):
        sentence_num = int(mentions.find('sentence').text)
        if mentions.get('representative'):
            origin_mention = mentions.find('text').text 
        else:
            text_pair = (origin_mention, mentions.find('text').text)
            num_s = int(mentions.find('start').text)
            num_e = int(mentions.find('end').text)
            corefer_dict[sentence_num].append(Corefer(text_pair, num_s, num_e))
            #corefer_dict[sentence_num] = (origin_mention, mentions.find('text').text)
for child in sentences.findall('sentence'):
    tokens = child.find('tokens')
    s_id = int(child.get('id'))
    """
    line = ''
    for words in child.iter('word'):
        line += words.text + ' '
    if corefer_dict[s_id] != []:
        r_mention, mention = corefer_dict[s_id].getPair()
        replace_word = '{}({})'.format(r_mention, mention)
        line = line.replace(mention, replace_word)
    print (line)
    """
    line = ''
    for child_t in tokens.findall('token'):
        t_id = int(child_t.get('id'))
        word = child_t.find('word').text + ' '
        if corefer_dict[s_id] != []:
            for corefers in corefer_dict[s_id]:
                s, e = corefers.getS_E()
                if s <= t_id < e:
                    word = ''
                elif t_id == e:
                    word = corefers.getReplace_w()
        line += word    
    print (line)    

