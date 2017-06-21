"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ:
name, aliases.name, tags.value, rating.value

色々調べて、
確証はなかったが、MongoDBそのものはbrewで、pymongoはpipでインストールできた。
jsonファイルの読み込みも皆さん色々トラブっているので、安全のため、python経由では
なく、直接。
 mongoimport --db test  --type json --file artist.json
--jsonArray は、この場合使えなくて、こっち。
mongo shellとかで、データベースが出来ているのを確認して、pymongoのtutorial通りに
やると、indexとかが出来た模様。

"""
#import gzip
#import json
import pymongo

begin = 0
end = 100

from pymongo import MongoClient
#client = MongoClient()
client = MongoClient('localhost',27017)
db = client.test

print("db:",db.name)
collection = db.artist
collection.create_index([("name", pymongo.ASCENDING)])
collection.create_index([("aliases.name", pymongo.ASCENDING)])
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])
