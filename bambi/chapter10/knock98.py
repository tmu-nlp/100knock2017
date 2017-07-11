from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import pickle
model = pickle.load(open("model96.pickle","rb"))
y = [v for k,v in model.items()]
Z = hierarchy.linkage(y[:20], 'ward')
plt.figure()
dn = hierarchy.dendrogram(Z)
plt.show()
