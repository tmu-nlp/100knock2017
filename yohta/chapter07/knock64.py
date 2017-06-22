import gzip
import json
import pymongo

# create artist at mongodb
client = pymongo.MongoClient()
artist_mongo_db = client.testdb
collection = artist_mongo_db.artist
heavy = []
counter = 0

with gzip.open('../data/artist.json.gz', 'rt') as artist_js:

    for line in artist_js:
        data = json.loads(line)
        heavy.append(data)
        counter += 1
        if counter == 5000:
            collection.insert_many(heavy)
            counter = 0
            heavy = []
            print('appended 5000 lines')
    if len(heavy) > 0:
        collection.insert_many(heavy)
        print('end of appending')

# create index
collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
