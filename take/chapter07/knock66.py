'''
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
'''

from pymongo import MongoClient, ASCENDING

client = MongoClient('localhost', 27017)
query = 'Japan'
print(client.DB_NAME.sample.find({'area': query}).count())
client.close()
