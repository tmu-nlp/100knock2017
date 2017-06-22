from pymongo import MongoClient

client = MongoClient()
db = client.my_database
co = db.my_collection

queen = co.find({'name': 'Queen'})
for line in queen:
    print(line)
