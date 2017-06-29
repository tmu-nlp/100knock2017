from pymongo import MongoClient

client = MongoClient()
db = client.MuicBrainz_DB
collection = db.artist_collection

for q in collection.find({"name":"Queen"}):
    print(q)

# find_one()で1つのドキュメントが取得出来ました。
# find()を使用すると、コレクションに登録されているドキュメントすべてが取得できます。
