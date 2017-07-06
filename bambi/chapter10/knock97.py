import pickle
from sklearn.cluster import KMeans
data = pickle.load(open("model96.pickle","rb"))
X = [v for k, v in data.items()]
kmeans = KMeans(n_clusters=5).fit(X)
print(kmeans.labels_)
