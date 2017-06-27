'''
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．

localhost:27017でmongodbがlistenしている状況（デフォルト）で、下記を実行する。
DB_NAMEは任意
$ mongoimport -h localhost --port 27017 --db DB_NAME --collection sample --file artist.json

さらに，次のフィールドでインデックスを作成せよ:
name
aliases.name
tags.value
rating.value
'''

from pymongo import MongoClient, ASCENDING
from pprint import pprint
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.DB_NAME
cl = db.sample

cl.create_index([("name",ASCENDING), ("aliases[].name",ASCENDING), ("tags[].value",ASCENDING), ("rating.value",ASCENDING) ])

start_time = time.time()
for data in cl.find({'name': 'Oasis'}):
    pprint(data)
print(time.time() - start_time, 'sec')

client.close()
