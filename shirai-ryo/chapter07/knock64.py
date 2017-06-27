import json
from pymongo import MongoClient
from pymongo import ASCENDING #昇順
# find().sort({'なんちゃら':1}) でもおkっぽい
# find().sort({'なんちゃら':-1}) だと降順ソートになる

client = MongoClient() # データベースに接続
db = client.MuicBrainz_DB # データベース(MuicBrainz_DB)を取得
collection = db.artist_collection # コレクションの取得

for line in open("artist.json", "r"):
    data = json.loads(line)
    collection.insert(data)

collection.create_index([("name", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
