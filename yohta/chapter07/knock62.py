import leveldb
#import json

artist_db = leveldb.LevelDB('../data/artist_db', create_if_missing=False)

tgt_area = input('search area:')
tgt_counter = 0
for key,value in artist_db.RangeIter():
#    name_ids = key.decode()
#    name,ids = name_ids.split('\t')
    area = value.decode()
    if area == '':
        area = '登録なし'

    if area == tgt_area:
        tgt_counter += 1
print("{} area's artists:\t{}".format(tgt_area,tgt_counter))
