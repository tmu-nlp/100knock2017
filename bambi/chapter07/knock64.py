from pymongo import MongoClient, ASCENDING
import json
if __name__ == "__main__":
    client = MongoClient()
    db = client.knock
    collection = db.artist
    count = 0
    for line in open('artist.json'):
        collection.insert_one(json.loads(line))
        if count == 4000:
            break # xx records will be enough for test, since file is too big to add, wasted memory
        count +=1
        
    #name, aliases.name, tags.value, rating.value
    collection.create_index([("name", ASCENDING)])
    collection.create_index([("rating.value", ASCENDING)])
    collection.create_index([("tags.value", ASCENDING)])
    collection.create_index([("aliases.name", ASCENDING)])    
    client.close()
    print("success")
