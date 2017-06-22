import json
import gzip
import pymongo

def json_loading(file_name):
    with gzip.open(file_name) as f:
        for line in f:
            if not(line is None):
                artist = json.loads(line.decode('utf-8'))
                yield artist

def make_db(file_name):
    client = pymongo.MongoClient()
    db = client.my_database
    db.drop_collection('artist')
    co = db.artist
    for i,dic in enumerate(json_loading(file_name)):
        co.save(dic)
        if i % 10000 == 0:
            print(i)
            print(dic)
    co.create_index([('name',pymongo.ASCENDING)])
    co.create_index([('aliases.name',pymongo.ASCENDING)])
    co.create_index([('tags.value',pymongo.ASCENDING)])
    co.create_index([('rating.value',pymongo.ASCENDING)])
 
if __name__ == '__main__':
    file_name = 'artist.json.gz'
    make_db(file_name)
