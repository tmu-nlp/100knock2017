#!python
import re

import sexpdata

from Parser import KnockSoup


def extract_words(s_exp):
  words = list()

  # if reach leaf, return word
  if sum(isinstance(sexp, sexpdata.Symbol) for sexp in s_exp) == 2:
    return [s_exp[1].value()]

  # if first element is symbol 
  if isinstance(s_exp[0], sexpdata.Symbol):
    s_exp = s_exp[1:]

  # search next chunks
  for next_s_exp in s_exp:
    words.extend(extract_words(next_s_exp))
  return words


def hoge(s_exp):
  words = list()

  if not isinstance(s_exp, list):
    return []
  if isinstance(s_exp[0], sexpdata.Symbol):
    if s_exp[0].value() == "NP":
      s_exp = s_exp[1:]
      words.append(extract_words(s_exp))
    elif isinstance(s_exp[1], list):
      s_exp = s_exp[1:]
    else:
      return []

  for sexps in s_exp:
    words.extend(hoge(sexps))
  return words

symbols = [("``", "StartQuote"), ("''", "EndQuote"), ("`", "StartQuote"), ("'", "EndQuote")]
re_num = re.compile("\d+")

def reverse_symbol(text, is_symbol=True):
  i = int(is_symbol)

  for from_to in symbols:
    text = text.replace(from_to[i-1], from_to[i])

  if is_symbol:
    text = re_num.sub(lambda x: "<num>{}</num>".format(x.group()), text)
  else:
    text = text.replace("<num>", "").replace("</num>", "")

  return text


def extract_s_exp(file_name):
  soup = KnockSoup(file_name)
  for s_exp in soup.find_all("parse"):
    print(s_exp)
    s_exp = reverse_symbol(s_exp.text, is_symbol=True)
    nps = hoge(sexpdata.loads(s_exp))
    print([reverse_symbol(" ".join(np), is_symbol=False) for np in nps])
    input()


if __name__ == "__main__":
    file_name = "head.txt.xml"
    extract_s_exp(file_name)
