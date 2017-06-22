import plyvel

my_db = plyvel.DB('artist.db', create_if_missing = True)
count = 0
for key, value in my_db:
    if value == b'Japan':
        count += 1
print(count)
