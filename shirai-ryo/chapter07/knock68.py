from pymongo import MongoClient

client = MongoClient()
db = client.MuicBrainz_DB
collection = db.artist_collection

for item in collection.find({"tags.value": "dance"}).sort("rating.count", -1).limit(10):
    print("{}\t{}".format(item["name"],item["rating"]["count"]))
