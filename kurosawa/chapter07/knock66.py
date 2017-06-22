import pymongo
from knock65 import conect_db

def get_artist(co):
    count = 0
    for data in co.find():
        if 'area' in data.keys():
            if data['area'] == 'Japan':
                count += 1

    return count

if __name__ == '__main__':
    co = conect_db()
    print(get_artist(co))
