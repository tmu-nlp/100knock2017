from pymongo import MongoClient

client = MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

for name in collection.find({"name": "Queen"}):
    print(name)

client.close()
