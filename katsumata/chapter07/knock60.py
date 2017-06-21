import redis
import json
import gzip

file_neme = 'artist.json.gz'
db = redis.Redis(host='localhost',port=6379, db = 0)

with gzip.open(file_name, 'r') as f_p:
    for line in f_p:
        obj = json.loads(line.decode('utf-8'))
        if not 'area' in obj:
            continue
        db.hset(obj['name'], 'area', obj['area'])
        """
        db.hset(obj['id'], 'name', obj['name']) 
        db.hset(obj['id'], 'area', obj['area'])
        """
