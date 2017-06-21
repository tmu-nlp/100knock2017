import pymongo

client = pymongo.MongoClient()

db = client.my_db
artist_co = db.artists

input_name = input('アーティストの別名は？\n')

for artist in artist_co.find({'aliases.name':input_name}):
    print (artist)
    print ()
