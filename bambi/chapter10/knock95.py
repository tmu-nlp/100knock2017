import scipy.stats
import pickle
human = []
data = open("combined.csv").readlines()[1:]
model = pickle.load(open("similar94.pickle","rb"))
words = [m[0] for m in model]
for d in data:
    d = d.strip("\n").split(",")
    key = d[0]+"\t"+d[1]
    if key in words:
        human.append((key, d[2]))
human = sorted(human, key = lambda x:x[1], reverse=True)
model = sorted(model, key = lambda x:x[1], reverse=True)
print(scipy.stats.spearmanr(human,model))
