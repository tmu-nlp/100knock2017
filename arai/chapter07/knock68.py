from pymongo import MongoClient

client = MongoClient()
db = client.my_database
co = db.my_collection

sort = co.find({'tags.value' : 'dance'}).sort('rating.count',-1).limit(10)
#sort({'rating.count' : -1})
for line in sort:
    #rating = co.find()sort({rating.count:-1})
    print(line['name'])
    
