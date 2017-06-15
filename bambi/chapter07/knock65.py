from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient()
    db = client.knock
    collection = db.artist
    for q in collection.find({"name": "Queen"}):
        print(q)
