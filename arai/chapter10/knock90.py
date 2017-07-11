from gensim.models import word2vec
import numpy as np
'''
sentences = word2vec.Text8Corpus('../chapter09/knock81.txt')

model = word2vec.Word2Vec(sentences)

model.save('knock90.model')
'''

word2vec = word2vec.Word2Vec.load('knock90.model')
print('{}\n{}\n'.format('(knock86)',word2vec['United_States']))

sim = np.dot(word2vec['United_States'], word2vec['US']) / (np.linalg.norm(word2vec['United_States']) * np.linalg.norm(word2vec['US']))
print('{}\n{}\n'.format('(knock87)',sim))


print('(knock88)')
sim_list = []
for i in word2vec.wv.vocab.keys():
    if i != 'England':
        sim = np.dot(word2vec['England'], word2vec[i]) / (np.linalg.norm(word2vec['England']) * np.linalg.norm(word2vec[i]))
        sim_list.append((i,sim))
for word, sim in sorted(sim_list, key = lambda x: x[1], reverse = True)[:10]:
    print(word, sim)

print('\n','(knock89)')
sim_list = []
for i in word2vec.wv.vocab.keys():
    vec = word2vec['Spain'] - word2vec['Madrid'] + word2vec['Athens']
    sim = np.dot(vec, word2vec[i]) / (np.linalg.norm(vec) * np.linalg.norm(word2vec[i]))
    sim_list.append((i,sim))

for word, sim in sorted(sim_list, key = lambda x: x[1], reverse = True)[:10]:
    print(word, sim)

