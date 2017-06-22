from pymongo import MongoClient

client = MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection
rank = dict()
for name in collection.find({'tags.value': 'dance', 'rating.count':{'$exists': True}}):
    for x in name:
        rank[name["name"]] = name['rating']['count']
i = 0
for k, v in sorted(rank.items(), key = lambda x:x[1], reverse = True):
    print(k, v)
    i += 1
    if i == 10:
        break

client.close()
