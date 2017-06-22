import redis

db = redis.Redis(host='localhost', port=6379, db= 0)

input_artist = input('アーティストの名前:').encode('utf-8')
#input_artist=(b'BadKlaat')
if db.hvals(input_artist) == []:
    print ('該当なし')
else:
    artist_area = db.hvals(input_artist).pop().decode('utf-8')
    print ('活動場所: {}'.format(artist_area))
