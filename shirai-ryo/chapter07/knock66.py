from pymongo import MongoClient

client = MongoClient()
db = client.MuicBrainz_DB
collection = db.artist_collection

for a in collection.find({"area":"Japan"}):
    print(a)
