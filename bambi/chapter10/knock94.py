from scipy import spatial
from gensim.models import *
import pickle
features = pickle.load(open("features85.pickle","rb"))
model = word2vec.Word2Vec.load('corpus90.model')
data = open("combined.csv").readlines()
ans = []
for line in data[1:]:
    words = line.strip("\n").split(",")
    if words[0] not in features or words[1] not in features:
        continue
    cos90 = model.wv.similarity(words[0], words[1])
    cos85 = 1 - spatial.distance.cosine(features[words[1]], features[words[0]])
    x = "{}\t{}\t{}\t{}\t{}".format(words[0],words[1],words[2],cos90,cos85)
    print(x)
    ans.append(x)

pickle.dump(ans,open("similar94.pickle","wb"))
print("finished")
