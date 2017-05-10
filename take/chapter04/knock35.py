'''
knock35. 
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

from knock30s import loadmecabdata

alllist = loadmecabdata()#1文を構成する形態素情報のマップのリスト
counter_max = -1
for sentence in alllist:
    counter = 0
    for i,word_dict in enumerate(sentence):
        if word_dict['pos'] == '名詞':
            counter += 1
            if counter == 10:
                print("max word:", word_dict['surface'])
        else:
            if counter_max < counter:
                counter_max = counter
            counter = 0

print(Ans. ",counter_max)
