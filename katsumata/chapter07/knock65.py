import pymongo

client = pymongo.MongoClient()

db = client.my_db
artist_co = db.artists

for artist in artist_co.find({'name':'Queen'}):
    print (artist)
    print ()
