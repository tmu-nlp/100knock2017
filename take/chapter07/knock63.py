'''
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
'''

import gzip
import json
import redis
from collections import defaultdict

r = redis.Redis()

with gzip.open('artist.json.gz', 'rt') as f:
    for i, l in enumerate(f):
        # print(i)
        data = json.loads(l)
        # print(data)
        # if r.exists(data['name']):
        #     print('duplicated name:{}'.format(data['name']))
        # reshaped_tag = defaultdict(lambda:0)
        reshaped_tag = dict()
        if "tags" in data:
            # r.hmset(data['name'], {'area':data['area']})
            # r.set(data['name'], data['area'])
            tags = data['tags']
            for tag in tags:#tagsはListで要素はdict型
                reshaped_tag[tag['value']] = tag['count']
                # print('{}\t{}:{}'.format(data['name'],tag['count'], tag['value']))
                # print('{}\t{}'.format(data['name'],tag))
                # print("name:{}\ttags:{}".format(data['name'], tag))
            # r.sadd(data['name'], data['area'])
            print('{}:\t{}'.format(data['name'], reshaped_tag))
            try:
                r.hmset(data['name'], reshaped_tag)
            except:
                print("rise exception")
        else:
            reshaped_tag[""] = 0
            try:
                r.hmset(data['name'], reshaped_tag)
            except:
                print("rise exception")
                
            # r.sadd(data['name'], 'notagso')

