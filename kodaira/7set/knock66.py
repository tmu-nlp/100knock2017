#!/usr/bin/python

import sys

from pymongo import MongoClient


if __name__ == "__main__":
  client = MongoClient('localhost', 27017)
  db = client.nlp100
  col = db.json_dict
  print("Area -> Japan:  ", col.find({'area':'Japan'}).count())
