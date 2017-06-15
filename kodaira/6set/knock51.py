#!usr/bin/python

from part50 import sentence_segment


def separate_word(file_name):
  return sentence_segment(file_name).replace("\n", "\n\n").replace(" ", "\n")


if __name__ == "__main__":
  file_name = "nlp.txt"
  print(separate_word(file_name))
