import pymongo

client = pymongo.MongoClient()

db = client.my_db
artist_co = db.artists

for i, artist in enumerate(artist_co.find({'tags.value':'dance'}).sort('rating.count', -1)):
    if i == 10:
        break
    print (artist['name'])
    print ()
