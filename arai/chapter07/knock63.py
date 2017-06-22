import plyvel
import json
import gzip

with gzip.open('artist.json.gz') as j_f:
    my_db = plyvel.DB('tag.db', create_if_missing = True)
    for line in j_f:
        data = json.loads(line.decode("utf-8"))
        if 'name' in data.keys() and 'tags' in data.keys():
            tag = json.dumps(data['tags'])
            my_db.put(data['name'].encode("utf-8"), tag.encode("utf-8"))

sample = my_db.get(b"Oasis")
my_db.close()
print(sample)
