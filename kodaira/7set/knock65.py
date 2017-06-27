#!/usr/bin/python

import sys
from pymongo import MongoClient
from types import *


p = lambda x, y: print("{}: {}".format(x, y))


def print_db_info(data_dict):
  for tag, info in data_dict.items():
    if type(info) is list:
      print(tag, end='\n\t')
      for tag2, info2 in info[0].items():
        p(tag2, info2)
    elif type(info) is dict:
      print(tag, end='\n\t')
      for tag2, info2 in info.items():
        p(tag2, info2)
    else:
      p(tag, info)
  print('\n') 

if __name__ == "__main__":
  client = MongoClient('localhost', 27017)
  db = client.nlp100
  col = db.json_dict
  for data_dict in col.find({'name':'Queen'}):
    print_db_info(data_dict)
