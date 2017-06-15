#!usr/bin/pythhon
# refarence: http://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5
# website: http://nlp.stanford.edu/software/corenlp.shtml
#
# make xml: java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt
# extra option: -ssplit.newlineIsSentenceBreak always


import sys

import Parser


def get_surface(token):
  return token.word.text


def extract_tokens(fname=None, get_func=get_surface, soup=None,
                   tags=["sentences", "sentence", "tokens", "token"]):
  soup = soup or Parser.KnockSoup(fname)
  return soup.extract_tokens(get_func=get_func, tags=tags)


def list2str(arrays, seps="\n"):
  if isinstance(seps, str):
    sep, seps = seps, seps
  elif isinstance(seps, list):
    sep, seps = seps[0], seps[1:]
    if seps == []:
      seps = "\n"
  else:
    return ""
  if len(arrays) == 0:
    return ""
  elif isinstance(arrays[0], (list, tuple)):
    return sep.join([list2str(array, seps=seps) for array in arrays if array])
  elif isinstance(arrays[0], str):
    return sep.join(arrays)
  else:
    return ""


if __name__ == "__main__":
  file_name = "head.txt.xml"
  sentences = extract_tokens(file_name)
  print(list2str(sentences, seps=["", "\n\n"]))
