import json
import gzip
import plyvel

with gzip.open('../data/artist.json.gz', 'r') as data_js:
    name_area_db = plyvel.DB('result/knock60_result.ldb', create_if_missing=True)
    for line in data_js:
        data_dict = json.loads(line.decode('utf-8'))
        if set(['name', 'area']).issubset(set(data_dict.keys())):
            name_area_db.put(data_dict['name'].encode('utf-8'), data_dict['area'].encode('utf-8'))
    name_area_db.close()
