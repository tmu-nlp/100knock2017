import pickle
import sys

sys.path.append("../9set/")
from knock87 import cos
from knock86 import GetVec

def calc_sim(word1, word2, calc_func):
  return calc_func(word1, word2)


def calc_sim(calculators, fname):
  f = open(fname); f.readline()
  results = list()
  for line in f:
    word1, word2, human_sim = line.strip().split(',')
    try:
      sims = list(map(lambda x: x(word1, word2), calculators))
    except:
      continue
    results.append("{} {:3f} {:.3f}".format(human_sim, *sims))

  f.close()
  return results


def calc_cos(mat, vocab):
  get_vec = GetVec(mat, vocab)

  def _calc_cos(word1, word2):
    sims = cos(get_vec(word1), get_vec(word2))
    return sims[0]

  return _calc_cos



if __name__ == "__main__":
  model_fname = './data/w2v_model_knock80.pkl'
  words_fname = './data/wordsim353/combined.csv'
  fout = './data/similarity_knock94.txt'
  
  w2v_model = pickle.load(open(model_fname, 'rb'))

  pca_mat = pickle.load(open("../9set/data/pca_mat.pkl", 'rb'))
  pca_vocab = pickle.load(open("../9set/data/vocab.pkl", 'rb'))
  pca_cos = calc_cos(pca_mat, pca_vocab)

  results = calc_sim([w2v_model.wv.similarity, pca_cos], words_fname)
  open(fout, 'w').write("\n".join(results))
