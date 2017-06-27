import pymongo
import pprint

client = pymongo.MongoClient()
artist_mongo_db = client.testdb
collection = artist_mongo_db.artist
counter = 0

another = str(input("artist's another name:"))

if collection.find({'aliases.name':another}).count() != 0:
    for method in collection.find({'aliases.name':another}):
        counter += 1
        print('\n------- collected number:{} -------\n'.format(counter))
        pprint.pprint(method)
else:
    print('artist having that another name is not found')
