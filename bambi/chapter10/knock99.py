import numpy as np
from sklearn.manifold import TSNE
import pickle
import matplotlib.pyplot as plt
data = pickle.load(open("model96.pickle","rb"))
X = [v for k,v in data.items()]
model = TSNE(n_components=2)
X_tsne = model.fit_transform(X) 
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], cmap=plt.cm.get_cmap("jet", 10))
plt.show()
