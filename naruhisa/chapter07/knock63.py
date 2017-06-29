import json
import gzip
import plyvel
import pickle

class TAG_ARTHISTS():
    def __init__(self, name, tags, tags_count):
        self.tags = tags
        self.tags_count = tags_count

    def getName(self):
        return self.name
    def getTags(self):
        return self.tags
    def getTags_count(self):
        return self.tags_count

my_db = plyvel.DB('database63', create_if_missing = True)
with gzip.open('artist.json.gz', 'r', 'utf-8') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        name = obj['name']
        if 'tags' in obj:
            tags = obj['tags']
        else:
            tags = 'none'
        if 'tags[].count' in obj:
            tags_count = ['tags[].count']
        else:
            tags_count = 'none'
        artist_i = TAG_ARTHISTS(name, tags, tags_count)

        my_db.put(pickle.dumps(name), pickle.dumps(artist_i))

print('アーティスト名')
name = input()
a_i = pickle.loads(my_db.get(pickle.dumps(name)))
print(a_i.getTags_count())
print(a_i.getTags())
my_db.close()
