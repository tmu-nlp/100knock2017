from scipy import spatial
import pickle
x = pickle.load(open("85.pickle","rb"))
america1 = x["United_States"]
america2 = x["US"]
result = 1 - spatial.distance.cosine(america1, america2)
print(result)
