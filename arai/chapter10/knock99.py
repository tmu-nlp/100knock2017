import pickle
import numpy
import sklearn.manifold
import matplotlib.pyplot as pyplot

c2v = pickle.load(open('knock96.dump', 'rb'))
country_name = list(c2v.keys())
mat = numpy.stack(c2v.values())
tsne = sklearn.manifold.TSNE(n_components = 2).fit_transform(mat)

pyplot.scatter(*tsne.T)
pyplot.savefig('tsne_knock99.png')
