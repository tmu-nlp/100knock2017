import pickle
from gensim.models import word2vec
import numpy as np

def cos_sim(v1, v2):
    if (np.linalg.norm(v1)*np.linalg.norm(v2) == 0):
        return 0
    return np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))

if __name__ == '__main__':
    with open('../chapter09/word_context_pca.dump', 'rb') as f:
        word85, model85 = pickle.load(f)

    model90 = word2vec.Word2Vec.load('model.w2v')
    with open('combined.tab', 'r') as i_f, open('sim_cos90.txt', 'w') as o_f90, open('sim_cos85.txt', 'w') as o_f85:
        for line in i_f:
            words = line.strip().split()
            if words[0] == 'Word':
                continue
            try:
                sim_90 = model90.similarity(words[0], words[1])
                o_f90.write(line.strip() + ' ' + str(sim_90) + '\n')
            except KeyError:
                print('some of {} are not in vocabulary' .format(words))
            try:
                vec1 = model85[word85[words[0]]]
                vec2 = model85[word85[words[1]]]
                sim_85 = cos_sim(vec1, vec2)
                o_f85.write(line.strip() + ' ' + str(sim_85) + '\n')
            except KeyError:
                pass
