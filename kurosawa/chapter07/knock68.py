import pymongo
from knock65 import conect_db

def get_artist(co):
    count = 0
    for data in co.find({'tags.value':'dance'},sort = [('rating.count',pymongo.DESCENDING)]):
#        if 'dance' in data.tags[0].value:
        print(data)
        print()
        count += 1
        if count >=10:
            break

if __name__ == '__main__':
    co = conect_db()
    get_artist(co)
