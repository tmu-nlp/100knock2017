"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現
（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」
のように，元の参照表現が分かるように配慮せよ．


"""
# coding: utf-8
#from collections import defaultdict

import re
import xml.etree.ElementTree as ET
from collections import defaultdict

xml_root = ET.parse('nlp.txt.xml')

beg = 2
end = 3

repre_d = defaultdict(lambda: 0)


for ii, coref in enumerate(xml_root.iterfind('./document/coreference/coreference')):
    if (ii+1 >= beg) and (ii+1 <= end):
        #print(*coref)
        for coref_mem in  coref.findall('mention'):
            if coref_mem.get('representative') == 'true':
                rep_word = coref.findtext('./mention/text')
                #print(rep_word)
            #print(coref_mem.get('representative', 'false'))
            else:
                sent_id = int(coref_mem.findtext('sentence'))
                start = int(coref_mem.findtext('start'))
                end = int(coref_mem.findtext('end'))

                if repre_d[(sent_id,start)] == 0:
                    repre_d[(sent_id,start)] = (end, rep_word)

for sentence in xml_root.iterfind('./document/sentences/sentence'):
    sent_id = int(sentence.get('id'))

    if (sent_id >= beg) and (sent_id <= end):
        rep_rest =0
        for token in sentence.iterfind('./tokens/token'):
            token_id = int(token.get('id'))

            if rep_rest == 0 and (sent_id, token_id) in repre_d:

                (end, rep_text) = repre_d[(sent_id, token_id)]

                print('[' + rep_text + '] (', end = '')
                rep_rest = end - token_id

            print(token.findtext('word'), end = '')

            if rep_rest > 0:
                rep_rest -= 1
                if rep_rest == 0:
                    print(')', end = '')

            print(' ', end = '')

        print()
