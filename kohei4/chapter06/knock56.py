"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現
（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」
のように，元の参照表現が分かるように配慮せよ．
--- 秋山　Note
<head>は、主幹？、多分　the とかを飛ばした始まり？ で使用せず。
Element Tree, Stanford Core NLP　の使い方等、素人の１００本ノックさん等を参考にした。
それを元に、Element Treeの呼び方工夫、デバックの為に文を指定出来るよう、ループの簡素化等の改編

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
                    # use defaultdict, so not check with 'in'
                    repre_d[(sent_id,start)] = (end, rep_word)
                    #無いなら、辞書型[文番号,開始単語ID]=(終了単語ID,元単語)

for sentence in xml_root.iterfind('./document/sentences/sentence'):
    sent_id = int(sentence.get('id'))
    #To edit sentence, get sentence itself

    if (sent_id >= beg) and (sent_id <= end):
        rep_rest =0
        for token in sentence.iterfind('./tokens/token'):
            token_id = int(token.get('id'))


            if rep_rest == 0 and (sent_id, token_id) in repre_d:
                #(文番号,単語ID)が、参照先辞書にあるか？

                (end, rep_text) = repre_d[(sent_id, token_id)]
                #あれば、終了単語IDと代表参照表現（参照元表現）を取り出す

                print('[' + rep_text + '] (', end = '')
                #まず、代表参照表現と括弧達
                rep_rest = end - token_id
                #参照先終了IDXから、開始IDX引いてRepTextに入れる。


            print(token.findtext('word'), end = '')
            #参照に関係ない所は単語ごとに、文を印刷

            if rep_rest > 0:
                rep_rest -= 1
                if rep_rest == 0:
                    print(')', end = '')
                    #参照元のオリジナル表現の最後に括弧入れる為に、残りを計算


            print(' ', end = '')
            #単語間の空白

        print()
