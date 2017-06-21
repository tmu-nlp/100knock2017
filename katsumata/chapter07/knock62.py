import redis

db = redis.Redis(host='localhost', port=6379, db=0)
counter = 0

#keyは名前が入ってる
for key in db.keys():
    if db.hvals(key).pop() == 'Japan'.encode('utf-8'):
        artist_name = key.decode('utf-8') 
        #print ('アーティスト名: {}'.format(artist_name))
        counter += 1
print (counter)        
