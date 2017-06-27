from pymongo import MongoClient
import sys


client = MongoClient()
db = client.my_database
co = db.my_collection

argvs =sys.argv[1]
artist = co.find({'aliases.name' : argvs})

for line in artist:
    print(line)
