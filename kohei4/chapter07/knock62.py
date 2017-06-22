"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""
import gzip
import json
import leveldb

begin = 0
end = 10

db = leveldb.LevelDB('./artist_db')

count = 0

for ii, data in enumerate(db.RangeIter()):
#    if ii >= begin and ii <= end:
        #print(list(data))
        #print(data[0].decode("utf-8", "ignore"), data[1].decode("utf-8", "ignore"))
        B = data[1].decode("utf-8", "ignore")
        #print(B)
        if B == 'Japan':
            count += 1
            #print(count)

print('Japan Musician No.:{}'.format(count))
