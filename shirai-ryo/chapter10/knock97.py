from sklearn.cluster import KMeans
import pickle
import numpy as np
from collections import defaultdict

country = pickle.load(open('96.dump', 'rb'))
country_names = country.keys()
country_mat = np.stack(country.values())
cluster = KMeans(n_clusters=5).fit(country_mat)

my_dict = defaultdict(list)
for key, value in zip(cluster.labels_, country_names):
    my_dict[key].append(value)
for i in range(5):
    print(my_dict[i])
