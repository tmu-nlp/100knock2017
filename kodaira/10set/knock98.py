# SciPy Hierarchical Clustering and Dendrogram Tutorial: 
# https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/

import pickle

import numpy
import sklearn.cluster
import scipy.cluster.hierarchy
import matplotlib.pyplot as pyplot


if __name__ == "__main__":
  c2v = pickle.load(open("country2vec_knock96.pkl", 'rb'))
  keys = list(c2v.keys())
  mat = numpy.stack(c2v.values())
  ward = sklearn.cluster.AgglomerativeClustering(n_clusters=5, linkage='ward').fit(mat)
  Z = scipy.cluster.hierarchy.linkage(mat, 'ward')

  dic = dict()


  pyplot.figure(figsize=(25, 10))
  pyplot.title("knock98")
  pyplot.xlabel("country name")
  pyplot.ylabel("distance")
  scipy.cluster.hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=keys)
  pyplot.savefig("./data/dendrogram_knock98.png")

