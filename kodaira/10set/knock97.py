import pickle

import numpy
import sklearn.cluster



if __name__ == "__main__":
  c2v = pickle.load(open("country2vec_knock96.pkl", 'rb'))
  keys = list(c2v.keys())
  mat = numpy.stack(c2v.values())
  km = sklearn.cluster.KMeans(n_clusters=5).fit(mat)

  dic = dict()
  for k, v in zip(km.labels_, keys):
    dic[k] = dic.get(k, list())
    dic[k].append(v)

  for i in set(km.labels_):
    print(" ||| ".join(dic[i]))

