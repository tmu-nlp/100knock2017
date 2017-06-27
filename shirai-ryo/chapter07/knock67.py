from pymongo import MongoClient

def find_aliases(collection, name):
    for a_name in collection.find({"aliases.name": name}):
        print(a_name)

client = MongoClient()
db = client.MuicBrainz_DB
collection = db.artist_collection
find_aliases(collection, "Queen")

# for a_name in collection.find({"aliases"}):
#     print("a_n")
