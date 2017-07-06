from scipy import spatial
from collections import defaultdict
import pickle
x = pickle.load(open("85.pickle","rb"))
result = defaultdict(float)
for t, v in x.items():
    similarity = 1 - spatial.distance.cosine(x['England'], x[t])
    result[t] = similarity
data = sorted(result.items(), key=lambda n:n[1], reverse=True)
for v in data[1:11]:
    # 0は0.999999…でEnglandが出るのでその次から
    print(v)
