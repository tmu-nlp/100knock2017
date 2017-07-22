import pickle
import numpy as np
import scipy.cluster.hierarchy
import matplotlib.pyplot as pyplot

country = pickle.load(open('96.dump', 'rb'))
country_names = list(country.keys())
country_mat = np.stack(country.values())
z = scipy.cluster.hierarchy.linkage(country_mat, 'ward')

pyplot.figure(figsize = (25, 10))
scipy.cluster.hierarchy.dendrogram(z, leaf_rotation = 90, leaf_font_size = 8, labels = country_names)
pyplot.savefig('dendrogram_knock9.png')
