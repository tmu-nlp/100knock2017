#!/usr/bin/python

import sys

from pymongo import MongoClient
import pymongo


if __name__ == "__main__":
  client = MongoClient('localhost', 27017)
  db = client.nlp100
  col = db.json_dict
  count = 0
  active_list = ['name', 'tags.value', 'rating.value']
  print('Rank  --Dance--                count')
  for one_dict in col.find({'tags.value':'dance'}).sort('rating.count', pymongo.DESCENDING):
    count += 1 
    print("No.{:2d}: {:25s}{:4d}".format( \
      count, one_dict['name'], one_dict.get("rating", {}).get("count", 0)))
    if count == 100:
      break
    
