import leveldb
#import json

artist_db = leveldb.LevelDB('../data/artist_db', create_if_missing=False)

artist = input('search artist:')
for key,value in artist_db.RangeIter():
    name_ids = key.decode()
    name,ids = name_ids.split('\t')
    if name == artist:
        area = value.decode()
        if area == '':
            area = '登録なし'
        print('{}\t{}\t{}'.format(name,ids,area))
