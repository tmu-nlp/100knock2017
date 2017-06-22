#!usr/bin/python
# sample input "Al Street"

import plyvel

from knock60 import use_db

@use_db("./level_db/", False)
def get_artist_area(db, artist_name):
  output = db.get(artist_name.encode())
  if output is not None:
    output = output.decode()
  return output

if __name__ == "__main__":
  print('artist_name:', end=" ")
  artist_name = input()

  output = get_artist_area(artist_name) 
  print("Artist: {}, Area: {}".format(artist_name, output))
