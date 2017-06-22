from xml.etree.ElementTree import *
from pprint import pprint
from get_sentence import get_sentence, get_sentence_list
import copy

# all_coreference_list = list()
# sent_list = list(get_sentence_list())

def insert_braket(_sub:str, _sent_id:int, _start:int, _end:int):
    sent_list_copy = copy.deepcopy(sent_list)
    _sent = sent_list_copy[_sent_id-1]
    bra_token = _sent[_start-1]
    ket_token = _sent[_end-2]
    _sent[_start-1] = '(' + bra_token
    _sent[_end-2] = ket_token + ')'
    # _sent.insert(0, _sub)
    _sent.insert(_start-1, _sub)
    return _sent

# ment_list = list()
def dump(node):
    for c in node:
        if c.tag == "coreference":
            # print(c.tag)
            next_iter = c.getiterator('mention')
            oldIsRepr = False
            # ment_list = list()
            for ment in next_iter:
                # print(ment.get('representative') == 'true')
                ment_dict = dict()
                currIsRepr = ment.get('representative') == 'true'
                if currIsRepr and not oldIsRepr:
                    pass
                    # print('-----this is Repr.-----')
                for m in list(ment):
                    # if currRepr == 'true' and not oldRepr == 'true':
                    #     print('this is Repr.')
                    # print('{}:{}'.format(m.tag, m.text))
                    ment_dict[m.tag] = m.text
                    ment_dict['repr'] = currIsRepr
                ment_list.append(ment_dict)
                oldIsRepr = currIsRepr
                # print('---')
        dump(c)

if __name__ == '__main__':

    all_coreference_list = list()
    ment_list = list()
    sent_list = list(get_sentence_list())

    tree = parse("nlp.txt.xml")
    root = tree.getroot()
    dump(root)
    
    # 知りたいidは、sentence id -1 , token id -1
    # coreferenceの解析結果で、sentenceid=46、start=3, end=8
    # target_sent = sent_list[45]
    # print('targetsent:',target_sent)
    # bra_token = target_sent[2]
    # ket_token = target_sent[6]
    #
    # target_sent[2] = "(" +bra_token
    # print(target_sent)
    
    # before_sent = sent_list[45]
    # print(before_sent)
    # after_sent = insert_braket(_sub='hoge', _sent_id=46, _start=3, _end=8)
    # print(' '.join(after_sent))
    
    
    # pprint(ment_list)
    
    substring = ''
    for m in ment_list:
        if m['repr']:
            substring = str(m['text'])
            continue
        print("-----",m['sentence'])
        print(' '.join(insert_braket( \
                        _sub=substring, \
                        _sent_id=int(m['sentence']), \
                        _start=int(m['start']), \
                        _end=int(m['end']))))
    
