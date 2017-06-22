#!usr/bin/python
# reference: http://blog.liris.org/2010/10/python3mongodb.html

import json

import plyvel


def use_db(dbpath, cim=False):
  def _use_db(func):
    def wrapper(*args):
      artist_db = plyvel.DB(dbpath, create_if_missing=cim)
      output = func(artist_db, *args)
      artist_db.close()

      return output

    return wrapper

  return _use_db


@use_db("./level_db", True)
def make_artist_db(db, file_name):
  for line in open(file_name):
    artist_dict = json.loads(line)
    db.put(artist_dict['name'].encode(), \
           artist_dict.get('area', 'None').encode())


if __name__ == "__main__":
  file_name = "artist.json"
  make_artist_db(file_name) 
