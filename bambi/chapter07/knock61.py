import plyvel
db = plyvel.DB('artists.db', create_if_missing=True)
test_key = b"Oasis"
print(db.get(test_key))
db.close()
