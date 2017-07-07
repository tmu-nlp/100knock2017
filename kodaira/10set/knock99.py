import pickle

import numpy
import sklearn.manifold
import matplotlib.pyplot as pyplot


if __name__ == "__main__":
  c2v = pickle.load(open("country2vec_knock96.pkl", 'rb'))
  keys = list(c2v.keys())
  mat = numpy.stack(c2v.values())
  tsne = sklearn.manifold.TSNE(n_components=2).fit_transform(mat)

  dic = dict()


  pyplot.scatter(*tsne.T)
  pyplot.title("knock99")
  for k, (v0, v1) in zip(keys, tsne):
    pyplot.annotate(k, xy=(v0, v1), size=8)
  pyplot.savefig("./data/tsne_knock99.png")


