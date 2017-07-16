from gensim.models import word2vec
import pickle
import numpy as np
data = open('combined.tab').readlines()
pca = pickle.load(open('../chapter09/knock85.txt', 'rb'))
w2v = word2vec.Word2Vec.load('knock90.model')

for line in data:
  words = line.strip().split()
  if sum(words[i] in w2v.wv for i in range(2)) == 2:
    sim = w2v.wv.similarity(words[0], words[1])
  else:
    sim = 0

  if sum(words[i] in pca for i in range(2)) == 2:
    sim2 = np.dot(pca[words[0]], pca[words[1]]) / (np.linalg.norm(pca[words[0]]) * np.linalg.norm(pca[words[1]]))
  else:
    sim2 = 0
  print('{}\t{}\t{}'.format(line.strip(), sim, sim2))
 
