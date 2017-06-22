import pymongo
import pprint

client = pymongo.MongoClient()
artist_mongo_db = client.testdb
collection = artist_mongo_db.artist
counter = 0

method = collection.find({'tags.value':'dance'})
method.sort('rating.count',pymongo.DESCENDING)

for ranker in method[0:10]:
    counter += 1

    print('\n------- rating rank:{} -------\n'.format(counter))
    voted = ranker['rating']['count']
#    pprint.pprint(voted)
    print('rating count:{}'.format(voted))
#    pprint.pprint('id:{}\tname:{}\t'.format(ranker['id'],ranker['name']))
    print('id:{}\t\tname:{}'.format(ranker['id'],ranker['name']))
