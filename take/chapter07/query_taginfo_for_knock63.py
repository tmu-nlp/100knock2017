import redis
import sys

args = sys.argv

r = redis.Redis()

for who in args[1:]:
    tags = r.hgetall(who)
    print(who)
    for k,v in tags.items():
        print('\tタグ:{}\t被タグ数:{}'.format(k.decode('utf-8'), v.decode('utf-8')))
    # print('{}\t{}'.format(who,tags))
