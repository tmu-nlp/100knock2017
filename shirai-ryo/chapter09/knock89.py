from scipy import spatial
from collections import defaultdict
import pickle
vec = pickle.load(open("85.pickle","rb"))
result = defaultdict(float)
compared = vec["Spain"] - vec["Madrid"] + vec["Athens"]
for t, v in vec.items():
    similarity = 1 - spatial.distance.cosine(compared, vec[t])
    result[t] = similarity
data = sorted(result.items(), key=lambda n:n[1], reverse=True)
for v in data[:10]:
    print(v)
