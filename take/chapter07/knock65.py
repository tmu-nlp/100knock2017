'''
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．
'''

from pymongo import MongoClient, ASCENDING
import time
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client.DB_NAME
cl = db.sample
cl.create_index([("name",ASCENDING)])

start_time = time.time()

for hoge in cl.find({'name': 'Queen'}):
    pprint(hoge)

print(time.time() - start_time, 'sec')

client.close()
