import plyvel
import pickle

my_db = plyvel.DB('database', create_if_missing = False)
print('活動場所を検索したいアーティスト：')
name = input()

area = pickle.loads(my_db.get(pickle.dumps(name)))
print('{}の活動場所は{}です' .format(name, area))
