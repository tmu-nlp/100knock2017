import pickle
import numpy as np

word2vec = pickle.load(open('knock85.txt', 'rb'))

sim = np.dot(word2vec['United_States'], word2vec['US']) / (np.linalg.norm(word2vec['United_States']) * np.linalg.norm(word2vec['US']))

print(sim)


