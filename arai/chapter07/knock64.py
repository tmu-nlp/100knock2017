from pymongo import MongoClient, ASCENDING
import json
import gzip


client = MongoClient()
db = client.my_database
co = db.my_collection
co.remove();
with gzip.open('artist.json.gz') as text:
    for line in text:
        co.insert_one(json.loads(line.decode("utf-8")))
        #for data in co.find():
            #print(data)

co.create_index([('name', ASCENDING)])
co.create_index([('aliases.name', ASCENDING)])
co.create_index([('tags.value', ASCENDING)])
co.create_index([('rating.value', ASCENDING)])


