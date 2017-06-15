#!usr/bin/python

import nltk
from part51 import separate_word


def stemming(file_name):
  stemmer = nltk.stem.PorterStemmer()
  pairs = list()
  for word in separate_word(file_name).split("\n"):
    pairs.append((word, stemmer.stem(word)))
  return pairs

if __name__ == "__main__":
  file_name = "head.txt"
  word_stem_pairs = stemming(file_name)
  print(*["\t".join(pair) for pair in word_stem_pairs], sep="\n")
