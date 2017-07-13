import pickle
import numpy
import scipy.cluster.hierarchy
import matplotlib.pyplot as pyplot

c2v = pickle.load(open('knock96.dump', 'rb'))
country_name = list(c2v.keys())
mat = numpy.stack(c2v.values())
z = scipy.cluster.hierarchy.linkage(mat, 'ward')

pyplot.figure(figsize = (25, 10))
scipy.cluster.hierarchy.dendrogram(z, leaf_rotation = 90, leaf_font_size = 8, labels = country_name)
pyplot.savefig('dendrogram_knock9.png')
