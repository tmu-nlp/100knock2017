import pymongo
import json
import gzip

file_name = 'artist.json.gz'

client = pymongo.MongoClient()

db = client.my_db
artists_co = db.artists
with gzip.open(file_name, 'r') as f_p:
    for line in f_p:
        obj = json.loads(line.decode('utf-8'))
        obj_id = artists_co.insert_one(obj).inserted_id
artists_co.create_index([('name', pymongo.ASCENDING)])        
artists_co.create_index([('alises.name', pymongo.ASCENDING)])
artists_co.create_index([('tags.value', pymongo.ASCENDING)])
artists_co.create_index([('rating.value', pymongo.ASCENDING)])
