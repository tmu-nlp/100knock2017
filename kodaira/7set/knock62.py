#!usr/bin/python

import plyvel

from knock60 import use_db


@use_db("./level_db/", False)
def count_artist_area(db, artist_area):
  count = 0
  artist_area = artist_area.encode()

  for _, area in db:
    if area == artist_area:
      count += 1

  return count 


if __name__ == "__main__":
  # area = "Japan"
  area = input("Input area: ")
  count = count_artist_area(area) 
  print("{}: {}".format(area, count))
