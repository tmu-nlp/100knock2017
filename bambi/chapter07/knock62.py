import plyvel
db = plyvel.DB('artists.db', create_if_missing=True)
count = 0
for key, value in db:
    if value == b"Japan":
        count += 1
print(count)
db.close()
