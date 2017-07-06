from gensim.models import *
import pickle
model = word2vec.Word2Vec.load('corpus90.model')
data = dict()
for l in open("country.txt"):
    l = l.strip("\n")
    try:
        print(model[l])
        data[l] = model[l]
    except:
        print("{} not in model".format(l))
        
pickle.dump(data,open("model96.pickle","wb"))
