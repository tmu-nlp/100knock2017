#!/usr/bin/python
# count neg_pos : cut -c 1-2 | sort | uniq -c

import random


def add_label(file_name, label):
  labeled_file = list()
  with open(file_name) as fin:
    while True:
      try:
        line = fin.readline()
      except UnicodeDecodeError:
        continue
      if line == '':
        break
      labeled_file.append(' '.join((label, line)) )
    return labeled_file


def make_random_text(pos_file_name, neg_file_name):
    pos_file = add_label(pos_file_name, '+1')
    neg_file = add_label(neg_file_name, '-1')
    text = pos_file + neg_file
    random.shuffle(text)
    return text


if __name__ == "__main__":
    pos_file_name = "rt-polarity.pos"
    neg_file_name = "rt-polarity.neg"

    random_text = make_random_text(pos_file_name, neg_file_name)

    open('sentiment.txt', 'w').write("".join(random_text))
