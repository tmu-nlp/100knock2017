import json
import gzip
import plyvel

def json_loading(file_name):
    with gzip.open(file_name) as f:
        for line in f:
            if not(line is None):
                artist = json.loads(line.decode('utf-8'))
                yield artist

def make_db(file_name):
    db = plyvel.DB('artist.ldb', create_if_missing=True)
    for i,dic in enumerate(json_loading(file_name)):
        if 'area' in dic.keys():
            db.put(dic['name'].encode('utf-8'),dic['area'].encode('utf-8'))
    db.close()

if __name__ == '__main__':
    file_name = 'artist.json.gz'
    make_db(file_name)
