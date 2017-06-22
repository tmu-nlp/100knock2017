import redis
import json
import gzip

file_name = 'artist.json.gz'
db_tag = redis.Redis(host='localhost',port=6379,db=1)

def make_db():
    with gzip.open(file_name, 'r') as f_p:
        for line in f_p:
            obj = json.loads(line.decode('utf-8'))
            if not 'tags' in obj:
                continue
            db_tag.hset(obj['name'], 'tags', obj['tags'])

if __name__ == '__main__':
    make_db()
    input_artist = input('アーティストの名前:').encode('utf-8') 
    input_artist = 'Agora'.encode('utf-8')
    if db_tag.hvals(input_artist) == []:
        print ('該当なし')
    else:
        tags_b = db_tag.hvals(input_artist).pop()
        tags = tags_b.decode('utf-8')
        print (tags)

