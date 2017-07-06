import pickle

word2vec = pickle.load(open('knock85.txt', 'rb'))
print(word2vec['United_States'])
