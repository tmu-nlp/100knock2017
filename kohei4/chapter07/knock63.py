"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）の
リストを検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""
import gzip
import json
import leveldb

begin = 0
end = 100

db = leveldb.LevelDB('./try_db')

if len(list(db.RangeIter(include_value = False))) < 1000:

    with gzip.open('artist.json.gz','rt') as ff:
        for ii, line in enumerate(ff):
#            if ii >= begin and ii <= end:
                json_line = json.loads(line)
                #print(json_line.items())
                key = json_line['name']
                if json_line.get('tags'):
                    value = json_line.get('tags')
                else:
                    value = []

                #print(json.dumps(value))
                db.Put(key.encode(), json.dumps(value).encode())

"""
[{"count": 1, "value": "polish rock"}, {"count": 1, "value": "new wave"}]
"""

name = input('Who ?　:')
for ii, data in enumerate(db.RangeIter()):
#    if ii >= begin and ii <= end:
        A = name.strip()
        B = data[0].decode("utf-8", "ignore")
        if A == B:
            tag_data = json.loads(data[1].decode())
            print('Tag for: {}'.format(name))
            if len(tag_data):
                for tag in tag_data:
                    print(tag['value'],tag['count'])
            else:
                print('No Tag')
