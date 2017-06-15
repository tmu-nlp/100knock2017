#!usr/vin/python

from part53 import extract_tokens, list2str


def get_info(token):
  return (token.word.text, token.lemma.text, token.pos.text)


if __name__ == "__main__":
  file_name = "head.txt.xml"
  sentences = extract_tokens(file_name, tags=[ "sentence", "token"],
                             get_func=get_info)

  print(sentences)
  # seps [paragraph, sentences, sentence, tokens, token, morph_pair]
  print(list2str(sentences, seps=["\n\n", "\n", "\t"]))
