import plyvel, json
db = plyvel.DB('artists.db', create_if_missing=True)
with open('artist.json', 'rb') as json_data:
    lines = json_data.readlines()
    for line in lines:
        data = json.loads(line)
        #need to check since s'times key not exist
        if "area" in data.keys() and "name" in data.keys():
            db.put(data["name"].encode("utf-8"),data["area"].encode("utf-8"))# encode to solve (expected bytes, got str)
            
db.close()
