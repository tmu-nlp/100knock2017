#!usr/bin/python

from part57 import extract_dependencies
from part53 import list2str
from collections import defaultdict


def dic2list(dic):
  svo_list = list()
  for v, type2so in filter(lambda x: len(x[1]) >= 2, dic.items()):
    svo_list.append([type2so["nsubj"], v, type2so["dobj"]])
  return svo_list


def extract_svo(file_name):
  deps_list = extract_dependencies(file_name)
  targets = ["nsubj", "dobj"]
  svo_list = list()
  for deps in deps_list:
    v2so = defaultdict(dict)
    for dtype, gov, dep  in filter(lambda x: x[0] in targets, deps):
      v2so[gov][dtype] = dep
    svo_list.extend(dic2list(v2so))
  return svo_list


if __name__ == "__main__":
    xml_name = "head.txt.xml"
    svo_list = extract_svo(xml_name)
    print(list2str(svo_list, seps=["\n", "\t"]))
