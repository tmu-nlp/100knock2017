import sklearn.cluster
import pickle
import numpy
from collections import defaultdict

c2v = pickle.load(open('knock96.dump', 'rb'))
country_names = c2v.keys()
mat = numpy.stack(c2v.values())
km = sklearn.cluster.KMeans(n_clusters = 5).fit(mat)

dic = defaultdict(list)
for k, v in zip(km.labels_, country_names):
  dic[k].append(v)
for i in range(5):
  print(dic[i])
