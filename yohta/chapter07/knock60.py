import plyvel
import json
import leveldb
import gzip

artist_db = leveldb.LevelDB('../data/artist_db',create_if_missing = True)

with gzip.open('../data/artist.json.gz','rt') as artist_js:
#with open('../data/artist.json','r') as artist_js:
#readlines = artist_js.readlines()
    for line in artist_js:
        data = json.loads(line)
#        key = data['name'] --> 複数いた時に出ない
        key = data['name'] + '\t' + str(data['id'])
#        print(key)
#        value = data['area']
        value = data.get('area')
        if value is None:
            value = ''
#        print(value)
        artist_db.Put(key.encode(),value.encode())
