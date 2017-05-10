def loadmecabdata():
    alllist = []
    s_list = []  # 一文を構成する形態素のマップを要素にもつリスト
    with open('neko.txt.mecab') as f:
        for line in f:
            if line == 'EOS\n':
                # print("eosだお")
                if len(s_list) > 0:
                    alllist.append(s_list.copy())
                    # print(s_list)
                    # print(alllist)
                    s_list.clear()
                continue
            # print(line, end='')
            d = {k: v for k, v in [f.split(":") for f in line.rstrip("\n").split(",")]}  # 一文を構成する各形態素のマップ
            s_list.append(d)
        return alllist

# sanity check
# for i in loadmecabdata():
#     for j in i:
#         if j['pos'] == '動詞':
#             print('動詞の表層系: ', j['surface']) # 31. 動詞の表層形をすべて抽出せよ．
#             print('動詞の原型　: ', j['base']) # 32. 動詞の原型をすべて抽出せよ．

# for l in alllist:
#     print(l)