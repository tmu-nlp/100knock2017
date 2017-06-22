"""
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．

mongod を走らせておく必要がある。
mongod --dbpath /usr/local/var/mongodb/


import subprocess
from multiprocessing import Process

class mongoStart:
  def f(self):
    cmd = "c:\\mongodb\\bin\\mongod --dbpath d:\\mongodb\\db"
    subprocess.call(cmd)

  def __init__(self):
    Process(target=self.f).start()

if __name__ == '__main__':
  mongoStart()
  print ("ok")

こんな方法で、スタートさせる方法があるらしいが、デーモンが走っていて再度走らせても
このデーモン（？）の複数排除してくれるが、os.system()等 追加すると、
親シェル窓を使ってしまうので、だめ。
只、mongoDBのインタラクティブシェルをpythonから打てるのか不明なので
不明なので、やってみた証拠をペースト。

Kohei-no-MacBook-Air:chapter07 kohei$ mongo
MongoDB shell version v3.4.4
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.4.4
Server has startup warnings:
2017-06-19T14:40:57.538+0900 I CONTROL  [initandlisten]
2017-06-19T14:40:57.538+0900 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2017-06-19T14:40:57.538+0900 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2017-06-19T14:40:57.538+0900 I CONTROL  [initandlisten]
2017-06-19T14:40:57.538+0900 I CONTROL  [initandlisten]
2017-06-19T14:40:57.538+0900 I CONTROL  [initandlisten] ** WARNING: soft rlimits too low. Number of files is 256, should be at least 1000
> use test
switched to db test
> db.artist.find({'area': 'Japan'}).count()
22821
> exit
bye
Kohei-no-MacBook-Air:chapter07 kohei$



"""
