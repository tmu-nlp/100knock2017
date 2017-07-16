from gensim.models import word2vec
import pickle
import numpy as np

pca = pickle.load(open('../chapter09/knock85.txt', 'rb'))
w2v = word2vec.Word2Vec.load('knock90.model')
family_data = open('family.txt').readlines()


for line in family_data:
  word = line.strip().split()
  if sum(word[i] in w2v.wv for i in range(3) ) == 3 :
    sim = w2v.most_similar(positive = [word[1], word[2] ], negative = [word[0]], topn = 1)
    print('{} {} {:.2f}'.format(word[3],*sim[0]), end ='\t')  
  else:
    print('{} {} {}'.format(word[3],'i', 0), end ='\t')  

  if sum(word[i] in pca for i in range(3)) == 3:
    vec = pca[word[1]] - pca[word[0]] + pca[word[2]]
    max_num = (0,'')
    for word2 in pca: 
      sim = np.dot(vec, pca[word2]) / (np.linalg.norm(vec) * np.linalg.norm(pca[word2]))
      if max_num[0] < sim:
        max_num = (sim, word2)
    print('{0} {2} {1:.2f}'.format(word[3], *max_num))
  else:
    print('{} {} {}'.format(word[3],'i', 0))  

     
