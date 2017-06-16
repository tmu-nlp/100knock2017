# Stanford Core NLPの共参照解析の結果に基づき，
# 文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

'''ex.
<coreference>
    <mention representative="true">
        <sentence>38</sentence>
        <start>4</start>
        <end>6</end>
        <head>5</head>
    </mention>
    <mention>
        <sentence>23</sentence>
        <start>13</start>
        <end>26</end>
        <head>13</head>
    </mention>
</coreference>
<coreference>...
'''





import xml.etree.ElementTree as et

with open('../data/nlp.txt.xml') as i_f,open('answer56.txt','w') as a_f:
    # sentence-id,token-id(start),token-id(end),coreferenceの辞書を作る
    coref = dict() #dict{(sent_id,rep_start_id),(rep_end_id,repre <-- str型)}
    par = et.parse(i_f)
    for xml in par.iterfind('./document/coreference/coreference'):
#        print(xml)
        # ~/mention(representative)/textの検索、text取得
        repre = xml.findtext('./mention[@representative="true"]/text')
#        print(repre)
        for mention in xml.iterfind('./mention'):
            # mentionがrepresentativeでないmentionの時、情報取得
            if mention.get('representative','None') == 'None':
                sent_id = int(mention.findtext('sentence'))
                token_start = int(mention.findtext('start'))
                token_end = int(mention.findtext('end'))

                if not (sent_id,token_start) in coref:
                    coref[(sent_id,token_start)] = (token_end,repre)


    #今度は実際の文章を見る
    for sentence in par.iterfind('./document/sentences/sentence'):
        sent_id = int(sentence.get('id'))
        rest_token = 0

        for token in sentence.iterfind('./tokens/token'):
            start_id = int(token.get('id'))

            if rest_token == 0 and (sent_id,start_id) in coref:
                (end_id,repre) = coref[(sent_id,start_id)]

                a_f.write('「' + repre + ' ( <-- ')
                rest_token = end_id - start_id

            a_f.write(token.findtext('word'))

            if rest_token > 0:
                rest_token -= 1
                if rest_token ==0:
                    a_f.write(') 」')

            a_f.write(' ')
        a_f.write('\n')
