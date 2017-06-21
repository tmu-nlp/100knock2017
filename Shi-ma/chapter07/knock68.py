import pymongo
import pprint

def sort_rating(collection, num):
    for part_sort_rating in collection.sort('rating.count', -1).limit(num):
        print(part_sort_rating['name'])

if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist
    sort_rating(collection.find({'$and':[{'tags.value':'dance'}, {'rating.count':{'$exists':True}}]}), 10)
