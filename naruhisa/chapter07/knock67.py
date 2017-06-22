from pymongo import MongoClient

client = MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection
print('別名検索')
n = input()
for name in collection.find({"aliases.name": n}):
    print(name)

client.close()
