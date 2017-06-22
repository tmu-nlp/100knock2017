from xml.etree.ElementTree import *
from pprint import pprint

all_sentences_list = list()

def dump(node):
    for c in node:
        if c.tag == "sentences":
            sent_iter = c.getiterator('sentence')
            for sent in sent_iter:
                sentId = sent.get('id')
                # print(sentId)
                a_sent_list = []
                tokens_iter = sent.getiterator('tokens')
                for token in tokens_iter:
                    for tok in list(token):
                        # print(tok[0].text)
                        a_sent_list.append(tok[0].text)
                all_sentences_list.append(a_sent_list)
        dump(c)

def get_sentence_list():

    tree = parse("nlp.txt.xml")
    root = tree.getroot()
    dump(root)
    return all_sentences_list

def get_sentence(_sentence_id:int ):
    if _sentence_id < 1:
        _sentence_id = 1
    return all_sentences_list[_sentence_id-1]

if __name__ == '__main__':

    # tree = parse("nlp.txt.xml")
    # root = tree.getroot()
    # dump(root)
    pprint(get_sentence_list())
# all_sentences_listのインデックスは元ファイルの sentence id-1 に対応
# for s in all_sentences_list[:10]:
#     print(s)

# def get_sentence_list():
#     return all_sentences_list
#
# def get_sentence(_sentence_id:int ):
#     if _sentence_id < 1:
#         _sentence_id = 1
#     return all_sentences_list[_sentence_id-1]
