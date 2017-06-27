import json
import gzip
import plyvel
import pickle

def json_loading(file_name):
    with gzip.open(file_name) as f:
        for line in f:
            if not(line is None):
                artist = json.loads(line.decode('utf-8'))
                yield artist

def make_db_tags(file_name):
    db = plyvel.DB('artist_tag.ldb', create_if_missing=True)
    for dic in json_loading(file_name):
        if 'tags' in dic.keys():
            db.put(dic['name'].encode('utf-8'),pickle.dumps(dic['tags']))
    db.close()

def get_db_tags():
    db = plyvel.DB('artist_tag.ldb', create_if_missing=True)
    tag_list = db.get(input('アーティスト名を入力してください>>').encode('utf-8'))
    if tag_list != None:
        str_tag = []
        tag_list = pickle.loads(tag_list)
        for tag in tag_list:
            str_tag.append(tag['value'])
        print('タグ：{}　被タグ数：{}'.format(', '.join(str_tag),len(tag_list)))
    else:
        print('No data')

if __name__ == '__main__':
    file_name = 'artist.json.gz'
    make_db_tags(file_name)
    get_db_tags()
