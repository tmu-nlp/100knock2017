from gensim.models import *
data = word2vec.LineSentence('corpus81.txt')
model = word2vec.Word2Vec(data, size=20)
model.save('corpus90.model')
print("knock86 = {}".format(model["United_States"]))
print("knock87 = {}".format(model.wv.similarity('United_States', 'US')))
knock88 = model.wv.most_similar(positive=['England']) # topn = 10 by default
print("\n")
for x in knock88:
    print("knock88 = {}".format(x))
knock89 = model.wv.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'])
print("\n")
for y in knock89:
    print("knock89 = {}".format(y))
