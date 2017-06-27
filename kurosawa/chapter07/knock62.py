import plyvel


def get_db_japan():
    count = 0
    db = plyvel.DB('artist.ldb', create_if_missing=True)
    for key, area in db:
        if area == 'Japan'.encode('utf-8'):
            count += 1
#            print(key.decode('utf-8'))
    print('日本で活動するアーティストの数：{}'.format(count))
    db.close()

if __name__ == '__main__':
    get_db_japan()
