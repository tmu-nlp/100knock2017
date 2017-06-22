#import plyvel
import json
import leveldb
import gzip

artist_tag_db = leveldb.LevelDB('../data/artist_tag_db',create_if_missing = True)

# create db
with gzip.open('../data/artist.json.gz','rt') as artist_js:
#with open('../data/artist.json','r') as artist_js:
#readlines = artist_js.readlines()
    for line in artist_js:
        data = json.loads(line)
#        key = data['name'] --> 複数いた時に出ない
        key = data['name'] + '\t' + str(data['id'])
#        print(key)
#        value = data['area']
        value = data.get('tags')
        if value is None:
            value = []
#        print(value)
        artist_tag_db.Put(key.encode(),json.dumps(value).encode())

# search tags
artist = input('artist:')

for key,value in artist_tag_db.RangeIter():
    name_ids = key.decode()
    name,ids = name_ids.split('\t')
    if name == artist:
        print("(id:{}) {}'s tags:".format(ids,name))
        tags = json.loads(value.decode())
        if len(tags) > 0:
            for tag in tags:
                print("{}\t{}counts".format(tag['value'],tag['count']))
        else:
            print('tags is not found')
