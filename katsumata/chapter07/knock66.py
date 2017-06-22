import pymongo

client = pymongo.MongoClient()

db = client.my_db
artist_co = db.artists

print (artist_co.find({'area':'Japan'}).count())
