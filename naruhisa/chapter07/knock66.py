from pymongo import MongoClient

client = MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

print(collection.find({"area": "Japan"}).count())

client.close()
