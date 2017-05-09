import plyvel, json
db = plyvel.DB('tags.db', create_if_missing=True)
with open('artist.json', 'rb') as json_data:
    lines = json_data.readlines()
    for line in lines:
        data = json.loads(line)
        if "name" in data.keys() and "tags" in data.keys():
            tags = json.dumps(data["tags"])
            db.put(data["name"].encode("utf-8"),tags.encode("utf-8"))# encode to solve (expected bytes, got str)
test_key = b"Oasis"
tag_content = db.get(test_key)
db.close()
print(tag_content)
