from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient()
    db = client.knock
    collection = db.artist
    print(collection.find({"area": "Japan"}).count())
