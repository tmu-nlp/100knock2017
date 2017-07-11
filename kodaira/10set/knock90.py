import bz2
import os
import pickle
import sys
import logging

from gensim.models import word2vec

sys.path.append("../9set")
from knock88 import cos
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def train(sentences, size=100, window=5, min_count=5, workers=2):
  model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=10, workers=2)
  return model


if __name__ == "__main__":
  model_name = "./data/w2v_model_knock80.pkl"
  
  if not os.path.isfile(model_name):
    fname = "../9set/data/enwiki_knock81.txt.bz2"
    sentences = word2vec.LineSentence(fname)
    model = train(sentences)
    pickle.dump(model, open(model_name, 'wb'))
  else:
    model = pickle.load(open(model_name, 'rb'))

  print("knock_86")
  united_states_vec = model.wv["United_States"]
  print(united_states_vec)

  print("knock_87")
  print(model.wv.similarity("United_States", "U.S"))

  print("knock_88")
  print(*model.most_similar(positive=["England"], topn=10), sep='\n')
  
  print("knock_89")
  print(*model.most_similar(positive=["Spain", "Athens"], 
                            negative=["Madrid"], topn=10), sep='\n')



