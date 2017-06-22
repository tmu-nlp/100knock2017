#!usr/bin/python
# option: arg[1] -> "construct" or "search"
# sample input "Burning Skies"

import json
import sys

import plyvel

from knock60 import use_db


@use_db("./level_db_63/", cim=True)
def make_artist_db(db, file_name):
  name_list = list()
  for line in open(file_name):
    tag_list = list()
    artist_dict = json.loads(line)
    if 'tags' in artist_dict:
      tag_list.append(artist_dict['tags'][0].get('value', "None"))
      tag_list.append(str(artist_dict['tags'][0]['count']))
      db.put(artist_dict['name'].encode(), \
             json.dumps(tag_list).encode() )


@use_db("./level_db_63/", cim=False)
def get_tag(db, name):
  area, num = json.loads(db.get(name.encode()))

  return (name, area, num)


if __name__ == "__main__":
    file_name = "artist.json"

    if len(sys.argv) != 2:
      print("Please input option 'construct' or 'search'")
      exit()

    if sys.argv[1] == "construct":
      make_artist_db(file_name)
    elif sys.argv[1] == "search":
      output = get_tag(input("Input artist name: "))
      print("Tag: {}, Num: {}".format(*output[1:]))
