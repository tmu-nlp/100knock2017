import json
import gzip
import pymongo

def conect_db():
    client = pymongo.MongoClient()
    db = client.my_database
    co = db.artist
    return co

def get_artist(co):
    for data in co.find():
        if data['name'] == 'Queen':
            print(data)
            print()

if __name__ == '__main__':
    co = conect_db()
    get_artist(co)
