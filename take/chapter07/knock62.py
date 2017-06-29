'''
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．

* memo
同じkeyについて、複数の異なるareaを取りうる。
areaが複数存在するアーティストについては、
ひとつでもJapanが含まれていればカウントすることにする。
'''
import redis

cnt = 0
r = redis.Redis()
allkeys = r.keys()

for key in allkeys:
    if r.sismember(key, 'Japan'):
        # print(r.smembers(key))
        cnt += 1

print('sol=',cnt)
