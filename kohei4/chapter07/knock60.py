"""
60. KVSの構築
Key-Value-Store (KVS) を用い，
アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

import gzip
import json
import leveldb

begin = 0
end = 10

db = leveldb.LevelDB('./try_db')

with gzip.open('artist.json.gz','rt') as ff:
    for ii, line in enumerate(ff):
        if ii >= begin and ii <= end:
            json_line = json.loads(line)
            #print(json_line.items())
            key = json_line['name']
            if json_line.get('area'):
                value = json_line['area']
            else:
                value = ''

            db.Put(key.encode(), value.encode())

print(len(list(db.RangeIter(include_value = False))))
