#!usr/bin/python

from collections import defaultdict, Counter
import random, pickle, math, os

import numpy
import sklearn.feature_extraction
import scipy


ppmi_file = "./data/ppmi_dic.pkl"

bottom = 10
cut_dim = int(10**5)


if os.path.isfile(ppmi_file):
  print("Load ppmi file")
  ppmi_dict = pickle.load(open(ppmi_file, "rb"))
  word_dict = pickle.load(open('./data/word.pkl', 'rb') )
  voc_set = set()
  for vs in ppmi_dict.values():
    voc_set.update(vs.keys())
else:
  print("Load files")
  context_dict = pickle.load(open('./data/context.pkl', 'rb'))
  co_occur_dict = pickle.load(open('./data/co_occur.pkl', 'rb'))
  word_dict = pickle.load(open('./data/word.pkl', 'rb'))
  word_count = sum(co_occur_dict.values())

  print('start store ppmi')
  ppmi_dict = defaultdict(dict) 
  voc_set = set()
  for pair, freq in sorted(co_occur_dict.items(), key=lambda x: x[1], reverse=True):
    if freq > bottom:
      word, cont = pair.split('\t')
      numer = word_count * freq;
      denom = word_dict[word] * context_dict[cont]
      if numer > denom:
        voc_set.update([cont])
        ppmi_dict[word][cont] = math.log(numer / float(denom))
    else:
      break
  pickle.dump(ppmi_dict, open(ppmi_file, "wb"))


print('start convert to matrix')
len(voc_set)
dict_vectorizer = sklearn.feature_extraction.DictVectorizer(dtype=numpy.float32)
voc_set = list(voc_set); random.shuffle(voc_set); voc_set = voc_set[:cut_dim]
dict_vectorizer.fit([Counter(voc_set)])
vocablary = list(ppmi_dict.keys())


mat = dict_vectorizer.transform(ppmi_dict.values())
print(mat.shape)

pickle.dump(vocablary, open("./data/vocab.pkl", "wb"))
pickle.dump(mat, open("./data/ppmi_mat.pkl", "wb"))
