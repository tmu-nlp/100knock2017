"""
80. コーパスの整形
文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである．
ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう．
そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
各トークンに以下の処理を施し，単語から記号を除去せよ．

トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
空文字列となったトークンは削除
以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
"""

import bz2
import re


if __name__ == "__main__":

    with bz2.open('enwiki-20150112-400-r100-10576.txt.bz2','rt') as ff,\
    open('80corpus.txt','w') as gg:

        front_p = re.compile(r'^[\.,!\?;:()\[\]\'"]*')
        end_p = re.compile(r'[\.,!\?;:()\[\]\'"]*$')
        for ii, line in enumerate(ff):
            #if ii >= 0 and ii <= 3:
                one_line = []
                for word in line.strip().split(' '):
                    word = re.sub(front_p,r'',word)
                    word = re.sub(end_p,r'',word)
                    word = word.rstrip('\n')
                    #print(len(word))

                    if len(word) == 0:
                        #print('here')
                        continue

                    one_line.append(word)

                if one_line:
                    print(*one_line, sep= ' ', file = gg)
