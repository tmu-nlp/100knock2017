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
    cos = model.wv.similarity(words[0], words[1])
    print("{}\t{}\t{}".format(words[0],words[1],cos))
    ans.append((words[0]+"\t"+words[1],words[2]))
pickle.dump(ans,open("similar94.pickle","wb"))
print("finished")
