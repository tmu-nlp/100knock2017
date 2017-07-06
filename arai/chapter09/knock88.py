import pickle
import numpy as np

word2vec = pickle.load(open('knock85.txt', 'rb'))
sim_list = []

for i in word2vec:
    if i != 'England':
        sim = np.dot(word2vec['England'], word2vec[i]) / (np.linalg.norm(word2vec['England']) * np.linalg.norm(word2vec[i]))
        sim_list.append((i,sim))
    
for word, sim in sorted(sim_list, key = lambda x: x[1], reverse = True)[:10]:
    print(word, sim)


