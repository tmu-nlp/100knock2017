import plyvel

with open('result/knock61_result.txt', 'w') as data_out:
    name_area_db = plyvel.DB('result/knock60_result.ldb', create_if_missing=True)
    for key, value in name_area_db:
        print('{}     {}'.format(key.decode('utf-8'), value.decode('utf-8')), file=data_out)
    name_area_db.close()
