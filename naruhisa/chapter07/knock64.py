from pymongo import MongoClient, ASCENDING
import json
import gzip

client = MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection
with gzip.open('artist.json.gz', 'r', 'utf-8') as f:
    for count, line in enumerate(f):
        collection.insert_one(json.loads(line.decode('utf-8')))
        print(count)
    collection.create_index([("name", ASCENDING)])
    collection.create_index([("rating.value", ASCENDING)])
    collection.create_index([("tags.value", ASCENDING)])
    collection.create_index([("aliases.name", ASCENDING)])
    client.close()
