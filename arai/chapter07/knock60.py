import  plyvel
import json
import gzip

with gzip.open('artist.json.gz') as j_f:
    my_db = plyvel.DB('artist.db', create_if_missing = True)
    for line in j_f:
        #print(j_f)
        data = json.loads(line.decode("utf-8"))
        if 'area' in data.keys() and 'name' in data.keys():
            my_db.put(data['name'].encode('utf-8'), data['area'].encode('utf-8'))
            print(my_db)
my_db.close()

#my_db = plyvel.DB()
