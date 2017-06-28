# valueはバイト列でなければいけないので、
# keyに対してdictやlist/などの構造化されたデータをひもづけてLevelDBに保存したい場合、シリアライズする必要があります

# pickle モジュールは Python のオブジェクトを直列化・非直列化するための機能を提供している。
# 直列化 (Serialize) というのはプログラミング言語においてオブジェクトをバイト列などの表現に変換することを指す。
# 非直列化 (Deserialize) はその逆で、バイト列を元にオブジェクトを復元することだ。

import json
import plyvel
import pickle

artist_name = str(input())

my_db = plyvel.DB("kn63.ldb", create_if_missing=True)

with open("artist.json", "r") as f:
    for line in f:
        obj = json.loads(line)
        if "name" in obj and "tags" in obj:
            tags = pickle.dumps(obj["tags"])
            my_db.put(obj["name"].encode("utf-8"), tags)

if my_db.get(artist_name.encode("utf-8")):
    t = my_db.get(artist_name.encode("utf-8")) # アーティストのタグ
    tag_list = pickle.loads(t)
    for tag in tag_list:
        print("tag:{}\tcount:{}".format(tag["value"], tag["count"]))
        # タグリストの "value" と "count" で取り出せるのは、下の例を参照

else:
    print("見つかりませんでした")

my_db.close()

# 例えば、Slipknot のタグリストはこんな感じになっている
# [{'value': 'alternative metal', 'count': 1}, {'value': 'nu metal', 'count': 1}, {'value': 'rap metal', 'count': 1}, {'value': 'metal', 'count': 1}, {'value': 'rock and indie', 'count': 1}, {'value': 'new metal', 'count': 1}]
