#!usr/bin/python

import re


def sentence_segment(file_name):  
  re_seg = re.compile("([.:;!?]) ([A-Z])")
  re_empty = re.compile("\n{2,}")
  segmented_text = re_seg.sub(lambda x: x.group().replace(" ", "\n"),
                              open(file_name).read())
  return re_empty.sub("\n", segmented_text)


if __name__ == "__main__":
  print(sentence_segment('head.txt'))
