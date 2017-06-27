import plyvel
import pickle

my_db = plyvel.DB('database', create_if_missing = False)
count = 0
for k, v in my_db:
    area = pickle.loads(my_db.get(k))
    if area == 'Japan':
        count += 1
print('日本を活動場所としているアーティストは{}組です' .format(count))
