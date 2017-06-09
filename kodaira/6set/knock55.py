#!usr/vin/python

from part53 import extract_tokens
import itertools


def get_person_name(token, delimiter="\t", tag="PERSON"):
  return token.word.text if (token.ner.text == tag) else ""


def flatten(arrays):
  while True:
    if isinstance(arrays[0], list):
      arrays = list(itertools.chain(*arrays))
    elif isinstance(arrays[0], str):
      break
  return arrays


def extract_parson_names(fname):
  persons = extract_tokens(file_name, tags=["token"], get_func=get_person_name)
  persons = flatten(persons)
  persons = set(persons)
  persons.discard("")

  return list(persons)


if __name__ == "__main__":
  file_name = "head.txt.xml"
  persons = extract_parson_names(file_name)
  print(*sorted(persons), sep='\n')
