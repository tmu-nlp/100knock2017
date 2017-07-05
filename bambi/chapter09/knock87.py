from scipy import spatial
import pickle
x = pickle.load(open("features85.pickle","rb"))
d1 = x["United_States"]
d2 = x["US"]
result = 1 - spatial.distance.cosine(d1, d2)
print(result)
