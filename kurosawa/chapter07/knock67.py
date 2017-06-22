import pymongo
from knock65 import conect_db

def get_artist(co):
    a = input('artist name >>')
    for data in co.find():
        if 'aliases' in data.keys():
#            print(data['aliases'][0]['name'])
            if data['aliases'][0]['name'] == a:
                print(data)
                print()

if __name__ == '__main__':
    co = conect_db()
    get_artist(co)
