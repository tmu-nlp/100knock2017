'''
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
'''

from pymongo import MongoClient, ASCENDING, DESCENDING
from pprint import pprint
import time

# client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.DB_NAME
cl = db.sample

cl.create_index([("name", ASCENDING), ("aliases[].name", ASCENDING)])
cl.create_index([("tag", ASCENDING), ("tags[].value", ASCENDING)])
cl.create_index([("rating.count", DESCENDING)])


while True:
    print('Enter tag: ', end='' )
    query = input()
    for out in cl.find({'tags.value':query}).sort('rating.count', DESCENDING).limit(10):
        pprint(out.get('name'))

client.close()

