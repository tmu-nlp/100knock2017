import json
import gzip
import plyvel
import pickle

my_db = plyvel.DB('database', create_if_missing = True)
with gzip.open('artist.json.gz', 'r', 'utf-8') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        name = obj['name']
        if 'area' in obj:
            area = obj['area']
        else:
            area = '無い'

        my_db.put(pickle.dumps(name), pickle.dumps(area))
my_db.close()
