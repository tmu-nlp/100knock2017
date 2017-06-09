#!usr/bin/python

# installation: pip install beautifulsoup4
import Parser

import bs4
import sys


def get_mention_contents(mention, tags=("sentence", "start", "end", "text")):
  return [int(content.text) - 1 if content.text.isdigit() else content.text \
          for content in mention.find_all(tags)]


def add_coreference(sentences, coreferences):
  for coreference in coreferences:
    for mention in coreference.find_all("mention"):
      if mention.get("representative", None) is not None:
        rep = mention.find('text').text
      else:
        sid, start, end, text = get_mention_contents(mention)
        if sum("|||" in word  for word in sentences[sid]) != 0:
          continue
        if " ".join(sentences[sid][start:end]) == rep:
          continue
        end -= 1
        sentences[sid][start] = "<<< {} ||| {}".format(rep, sentences[sid][start])
        sentences[sid][end] = "{} >>>".format(sentences[sid][end])

  return sentences


def main(file_name):
  tags = ["sentence", "token"]
  soup = Parser.KnockSoup(file_name)
  sentences = soup.extract_tokens(get_func=lambda x: x.word.text, tags=tags)
  coreferences = soup.find_all("coreference")[1:]
  sentences = add_coreference(sentences, coreferences)
  return sentences



if __name__ == "__main__":
    file_name = "head.txt.xml"
    sentences = main(file_name)
    print(*[" ".join(sent) for sent in sentences if sent], sep="\n")
