"""
661. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

import gzip
import json
import leveldb

begin = 0
end = 10

db = leveldb.LevelDB('./artist_db')

name = input('Who ?　:')

for ii, data in enumerate(db.RangeIter()):
#    if ii >= begin and ii <= end:
        #print(list(data))
        #print(data[0].decode("utf-8", "ignore"), data[1].decode("utf-8", "ignore"))
        A = name.strip()
        B = data[0].decode("utf-8", "ignore")
        if A == B:
            print('Exactly Match!')
            print('Musician:{}\tActivity Area :{}'.\
            format(B,data[1].decode("utf-8", "ignore")))
        """
        else:
            if len(set(A) & set(B)) > 3:
                print('May be you want')
                print('Musician:{}\tActivity Area :{}'.\
                format(B,data[1].decode("utf-8", "ignore")))
        """
