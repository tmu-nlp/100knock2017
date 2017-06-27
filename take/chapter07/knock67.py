'''
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
'''

from pymongo import MongoClient, ASCENDING
from pprint import pprint
import time

# client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.DB_NAME
cl = db.sample

cl.create_index([("name",ASCENDING), ("aliases[].name",ASCENDING)])

while True:
    print('Enter aliases name: ', end='' )
    query = input()
    # out = cl.find({"aliases.name":query})
    for out in cl.find({"aliases.name":query}):
        pprint(out)

client.close()

