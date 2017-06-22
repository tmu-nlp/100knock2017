from pymongo import MongoClient

client = MongoClient()
db = client.my_database
co = db.my_collection

print(co.find({'area': 'Japan'}).count())
