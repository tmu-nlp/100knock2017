import plyvel

my_db = plyvel.DB('kn60.ldb', create_if_missing=True)

count = 0
for name, area in my_db:
    if area == b'Japan':
        count += 1

print(count)
# 22128であってる？

my_db.close()
