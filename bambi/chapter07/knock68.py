from pymongo import MongoClient
from collections import Counter
if __name__ == "__main__":
    client = MongoClient()
    db = client.knock
    collection = db.artist
    data = collection.find({"tags.value": "dance", "rating.count":{"$exists": True}})
    ranks = []
    for x in data:
        #print(x)
        rate_cnt = x["rating"]["count"]
        #print("wwww" + x["name"])
        if len(ranks) < 10:
            ranks.append(x)
        elif rate_cnt > ranks[-1]["rating"]["count"]:
            ranks[-1] = x
        # after更新リスト、順位も更新
        ranks = sorted(ranks, key=lambda r:r["rating"]["count"], reverse=True)
    
    for x in ranks:
        print("{}, {}".format(x["name"],x["rating"]["count"]))
