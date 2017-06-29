#!/usr/bin/python
# count neg_pos : cut -c 1-2 | sort | uniq -c

from collections import defaultdict
import re

def count_word(file_name, word_dict):
  for line in open(file_name):
    for word in line.strip().split()[1:]:
      word_dict[word] += 1

  return word_dict


def make_stop_list(fname):
  word_dict = defaultdict(int)
  non_stop_list = ['funny', 'good', 'like', 'comedy', 'love']

  count_word(fname, word_dict)

  stop_list = list()
  for word, freq in sorted(word_dict.items(), key = lambda x: -x[1]):
    if freq > 200 or len(word) < 3 or r'[0-9]' in word:
      if not word in non_stop_list:
        stop_list.append(word)

  return stop_list


def check_stop_word(word, stop_list):
  if word in stop_list:
    return True
  else:
    return False


if __name__ == "__main__":
  fname = "sentiment.txt"
  stop_list = make_stop_list(fname)

  print(stop_list)

  exit()
  for line in open(pos_file_name):
      for word in line.strip().split():
         print(word, check_stop_word(word, stop_list))
