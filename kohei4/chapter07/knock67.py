"""
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．

mongod を走らせておく必要がある。
mongod --dbpath /usr/local/var/mongodb/
このデーモン（？）の複数排除してくれるので、os.system()等 追加すると、
親シェル窓を使ってしまうので、だめ。
66当たりから気になっていたのだが、突如、Unixでは、crontabだったと思い出した。
起動時に走らせるのが常識で、shellで後から走らせるのは、実験のみと。。。

"""
#import gzip
import json
import pymongo
import os
import subprocess

begin = 0
end = 100

#subprocess.call('mongod --dbpath /usr/local/var/mongodb/ ', shell=True )


from pymongo import MongoClient
#client = MongoClient()
client = MongoClient('localhost',27017)
db = client.test


print("db:",db.name)
collection = db.artist

alias = input("Alias Name ? ")

count = collection.find({"aliases.name": alias}).count()
print('Found {} data'.format(count))
for ii, data in enumerate(collection.find({"aliases.name": alias })):
    print('Item: {}'.format(ii))
    for key, value in data.items():
        print('key = {}, value = {}'.format(key, value))



#takuro_count = collection.find({"name": "吉田拓郎"}).count()
#print('takuro_count:{}'.format(takuro_count))
