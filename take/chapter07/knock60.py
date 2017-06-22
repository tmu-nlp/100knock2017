'''
Usage:
Need redis to run.
before execution, start redis-server by following cmd.

$ redis-server

'''

import gzip
import json
import redis

r = redis.Redis()

with gzip.open('artist.json.gz', 'rt') as f:
    for i, l in enumerate(f):
        print(i)
        data = json.loads(l)
        if "area" in data:
            print("name:{}\tarea:{}".format(data['name'], data['area']))
            r.sadd(data['name'], data['area'])
        else:
            r.sadd(data['name'], 'unk')
