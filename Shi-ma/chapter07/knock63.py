import json
import gzip
import plyvel
import pickle

def make_name_tags_DB(data_js_path):
    with gzip.open(data_js_path, 'r') as data_js:
        name_tags_db = plyvel.DB('result/knock63_result.ldb', create_if_missing=True)
        for line in data_js:
            data_dict = json.loads(line.decode('utf-8'))
            if set(['name', 'tags']).issubset(set(data_dict.keys())):
                name_tags_db.put(data_dict['name'].encode('utf-8'), pickle.dumps(data_dict['tags']))
        name_tags_db.close()

def load_make_tags_DB(data_ldb_path, data_out_path):
    with open(data_out_path, 'w') as data_out:
        name_tags_db = plyvel.DB(data_ldb_path, create_if_missing=True)
        for key, tags_serialized in name_tags_db:
            tags_dict = pickle.loads(tags_serialized)
            print(key, file=data_out)
            print(tags_dict, file=data_out)
        name_tags_db.close()

if __name__ == '__main__':
    data_js_path = '../data/artist.json.gz'
    data_ldb_path = 'result/knock63_result.ldb'
    data_out_path = 'result/knock63_result.txt'
    make_name_tags_DB(data_js_path)
    load_make_tags_DB(data_ldb_path, data_out_path)
