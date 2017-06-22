"""
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．
> db.artist.find({name:"Queen"})
{ "_id" : ObjectId("5946348297cb68854e9c6bf5"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5946348397cb68854e9d32d5"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5946348597cb68854e9eed9f"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }

mongod を走らせておく必要がある。
mongod --dbpath /usr/local/var/mongodb/
このデーモン（？）の複数排除してくれるので、os.system()等 追加すると、
親シェル窓を使ってしまうので、だめ。

"""
#import gzip
#import json
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

who = input("Who do you want ?  ")

count = collection.find({"name": who}).count()
print('Found {} data'.format(count))
for data in collection.find({"name": who }):
    print(data)


#takuro_count = collection.find({"name": "吉田拓郎"}).count()
#print('takuro_count:{}'.format(takuro_count))
