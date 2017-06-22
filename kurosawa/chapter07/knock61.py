import plyvel


def get_db():
    db = plyvel.DB('artist.ldb', create_if_missing=True)
    name = input('artistを入力してください>>')
    area = db.get(name.encode('utf-8'))
    if area != None:
        print('活動場所：{}'.format(area.decode('utf-8')))
    else:
        print('No data')
    db.close()

if __name__ == '__main__':
    get_db()
