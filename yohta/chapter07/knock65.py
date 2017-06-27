# shell
"""
 > show dbs
 admin   0.000GB
 local   0.000GB
 testdb  0.135GB
 > use testdb
 switched to db testdb
 > show collections
 artist
 > db.artist.find({'name':'Queen'});
 { "_id" : ObjectId("594aa13ea0780309cc48b4b7"), "aliases" : [ { "sort_name" : "Queen", "name" : "Queen" } ], "id" : 701492, "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "gender" : "Female", "ended" : true, "area" : "Japan", "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "sort_name" : "Queen", "type" : "Character", "name" : "Queen" }
 { "_id" : ObjectId("594aa140a0780309cc497b63"), "aliases" : [ { "sort_name" : "女王", "name" : "女王" } ], "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "rating" : { "count" : 24, "value" : 92 }, "name" : "Queen", "begin" : { "month" : 6, "year" : 1970, "date" : 27 }, "id" : 192, "type" : "Group", "area" : "United Kingdom", "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "sort_name" : "Queen", "ended" : true }
 { "_id" : ObjectId("594aa145a0780309cc4b35bb"), "id" : 992994, "ended" : true, "name" : "Queen", "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen" }
"""



#import json
import pymongo
import pprint

client = pymongo.MongoClient()
artist_mongo_db = client.testdb
collection = artist_mongo_db.artist
counter = 0

for method in collection.find({'name':'Queen'}):
    counter += 1
    print('\n------- collected number:{} -------\n'.format(counter))
    pprint.pprint(method)
