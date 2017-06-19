import xml.etree.ElementTree as ET
from collections import defaultdict
from knock53 import xml_parse

if __name__ == '__main__':
    root = xml_parse('nlp.txt.xml')
    ch_list = defaultdict(list)
    for coref in list(root.getiterator('coreference')):
        for sen in list(coref):
            if sen.tag == 'mention':
                if sen.get('representative') == 'true':
                    text_ch = sen.findtext('text')
#                    print(text_ch)
                else:
                    sentence = sen.findtext('sentence')
                    start = sen.findtext('start')
                    end = sen.findtext('end')
                    text = sen.findtext('text')
                    text_com = text_ch + ' ( ' + text + ' )'
                    ch_list[sentence].append([start,end,text,text_com])
#    print(ch_list)
    for sen in list(root.getiterator('sentence')):
        idx = sen.get('id')
        if not(idx is None):
            str_list = []
            ch = ch_list[idx]
#            print(ch)
            for token in list(sen.getiterator('token')):
                token.get('id')
                str_list.append(token.findtext('word'))
            str_print = ' '.join(str_list)
            for change in ch:
                str_print = str_print.replace(change[2],change[3])
            print(str_print)
#    print(ch_list)
#        if word_.findtext('NER') == 'PERSON':
#            print(word_.findtext('word'))
