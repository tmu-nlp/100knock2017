#!/usr/bin/python

import sys

from pymongo import MongoClient

from knock65 import *


if __name__ == "__main__":
  client = MongoClient('localhost', 27017)
  db = client.nlp100
  col = db.json_dict
  aliases_name = 'Queen' #raw_input()
  for one_dict in col.find({'aliases.name':'Queen'}):
    print_db_info(one_dict)
