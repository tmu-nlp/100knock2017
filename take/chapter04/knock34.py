'''
例こんなやつを取り出す
surface:不可思議,base:不可思議,pos:名詞,pos1:形容動詞語幹
surface:の,base:の,pos:助詞,pos1:連体化
surface:太平,base:太平,pos:名詞,pos1:一般
'''

from knock30s import loadmecabdata

alllist = loadmecabdata()#1文を構成する形態素情報のマップのリスト
# i = 0 # sanity chk
for sentence in alllist:#
    # sanity chk
    # i += 1
    # print(sentence)
    # if i == 3:
    #     break
    # continue
    for i,word_dict in enumerate(sentence):
        #"の"が出てきたときその前後をみたいので、最初と最後の単語は検索対象からはずす
        if i == 0 or i == len(sentence)-1:
            continue
        if word_dict['base'] == 'の' and word_dict['pos'] == '助詞' \
            and word_dict['pos1'] == '連体化':
            if sentence[i-1]["pos"] == '名詞' and sentence[i+1]['pos'] == '名詞':
                print("hit: {}, {}".format(sentence[i-1]["surface"],sentence[i+1]["surface"]))
