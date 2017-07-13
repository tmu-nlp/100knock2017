import pickle
from  gensim.models import word2vec

country_file = open('../chapter09/country.txt').readlines()
w2v = word2vec.Word2Vec.load('knock90.model')
c2v = dict()

for line in country_file:
  line = line.strip()
  words = line.replace(' ', '_')
  if words in w2v.wv:
    country_vec = w2v[words]
    c2v[words] = country_vec
pickle.dump(c2v, open('knock96.dump', 'wb'))
