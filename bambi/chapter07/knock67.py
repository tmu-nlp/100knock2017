from pymongo import MongoClient
def find_aliases(collection, x):
    for q in collection.find({"aliases.name": x}):
        print(q) 
if __name__ == "__main__":
    client = MongoClient()
    db = client.knock
    collection = db.artist
    find_aliases(collection,"Queen")
    
