import pickle
import numpy as np
import sklearn.manifold
import matplotlib.pyplot as pyplot

country = pickle.load(open('96.dump', 'rb'))
country_names = list(country.keys())
country_mat = np.stack(country.values())
tsne = sklearn.manifold.TSNE(n_components = 2).fit_transform(country_mat)

pyplot.scatter(*tsne.T)
pyplot.savefig('tsne_knock99.png')
