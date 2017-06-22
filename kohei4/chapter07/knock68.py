"""
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多い
アーティスト・トップ10を求めよ．

mongod を走らせておく必要がある。
mongod --dbpath /usr/local/var/mongodb/
このデーモン（？）の複数排除してくれるので、os.system()等 追加すると、
親シェル窓を使ってしまうので、だめ。
66当たりから気になっていたのだが、突如、Unixでは、crontabだったと思い出した。
起動時に走らせるのが常識で、shellで後から走らせるのは、実験のみと。。。

tagsのDataは、一部、辞書型の入れ子


"""
#import gzip
import json
import pymongo
import os
import subprocess

begin = 0
end = 10

#subprocess.call('mongod --dbpath /usr/local/var/mongodb/ ', shell=True )


from pymongo import MongoClient
#client = MongoClient()
client = MongoClient('localhost',27017)
db = client.test


print("db:",db.name)
collection = db.artist

#alias = input("Alias Name ? ")

#count = collection.find({"tag.value": "dance"}).count()
dance = []
#print(count)
for ii, data in enumerate(collection.find({"tags.value": "dance" })):
    #if ii >= begin and ii <= end:
        #print(data)
        #print('Item: {}'.format(ii))
        #for key, value in data.items():
        #    print('key = {}, value = {}'.format(key, value))
        if "rating" in data:
            #data is dict type
            dance.append([data["name"],data["rating"]["count"]])

dance_sorted = sorted(dance, key=lambda x:x[1], reverse=True)

#print(dance)
for i, top_dancer in enumerate(dance_sorted):
    if i > 8:
        break

    print(top_dancer[0],top_dancer[1])




#takuro_count = collection.find({"name": "吉田拓郎"}).count()
#print('takuro_count:{}'.format(takuro_count))
