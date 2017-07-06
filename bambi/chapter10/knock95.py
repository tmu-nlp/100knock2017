import scipy.stats
import pickle
import numpy as np
human = []
data = open("combined.csv").readlines()[1:]
model = pickle.load(open("similar94.pickle","rb"))
words = [m[0] for m in model]
model90 = [m.split("\t")[3] for m in model]
human = [m.split("\t")[2] for m in model]
model85= [m.split("\t")[4] for m in model]

print(scipy.stats.spearmanr(human,model90, axis=None))
print(scipy.stats.spearmanr(human,model85, axis=None))#axis=None, then both arrays will be raveled
