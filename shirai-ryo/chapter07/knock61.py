import plyvel

X = str(input())

my_db = plyvel.DB('kn60.ldb', create_if_missing=True)

if my_db.get(X.encode('utf-8')):
    # value1 = my_db.get('key1') という求め方
    print(my_db.get(X.encode('utf-8')))
else:
    print("見つかりませんでした")

my_db.close()
