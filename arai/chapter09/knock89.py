import pickle
import numpy as np

word2vec = pickle.load(open('knock85.txt', 'rb'))
sim_list = []

for i in word2vec:
    vec = word2vec['Spain'] - word2vec['Madrid'] + word2vec['Athens']
    sim = np.dot(vec, word2vec[i]) / (np.linalg.norm(vec) * np.linalg.norm(word2vec[i]))
    sim_list.append((i,sim))
    
for word, sim in sorted(sim_list, key = lambda x: x[1], reverse = True)[:10]:
    print(word, sim)


