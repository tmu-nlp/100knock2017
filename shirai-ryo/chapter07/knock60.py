import json
import plyvel

my_db = plyvel.DB('kn60.ldb', create_if_missing=True)  # なければつくる

with open("artist.json", "r") as f:
    for line in f:
        obj = json.loads(line)
        if "name" in obj and "area" in obj:
            my_db.put(obj["name"].encode("utf-8"), obj["area"].encode("utf-8"))

my_db.close()


# import json
# import gzip
# import plyvel
#
# my_db = plyvel.DB('kn60.ldb', create_if_missing=True)  # なければつくる
#
#
#
# with gzip.open("artist.json.gz", "r") as f:
#     for line in f:
#         obj = json.loads(line)
#         if "name" in obj and "area" in obj:
#             my_db.put(obj["name"].encode("utf-8"), obj["area"].encode("utf-8"))
#     my_db.close()
#
# #for name, area in my_db:
#            # print("{}\t{}".format(key, value))
