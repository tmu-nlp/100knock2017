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
    with open('ccc.txt', 'r') as i_f, open('ccc_cos90.txt', 'w') as o_f90, open('ccc_cos85.txt', 'w') as o_f85:
        for line in i_f:
            words = line.strip().split()
            try:
                for l in model90.most_similar(positive = [words[1], words[2]], negative = [words[0]], topn = 1):
                    result_90 = l
                o_f90.write(line.strip() + ' ' + result_90[0] + ' ' + str(result_90[1]) + '\n')
            except KeyError:
                print('some of {} are not in vocabulary' .format(words))
            try:
                result_85 = 0
                vec1 = model85[word85[words[0]]]
                vec2 = model85[word85[words[1]]]
                vec3 = model85[word85[words[2]]]
                for word in word85:
                    vec = model85[word85[word]]
                    sim = cos_sim(vec2 - vec1 + vec3, vec)
                    if sim > result_85:
                        result_85 = sim
                        word_85 = word
                o_f85.write(line.strip() + ' ' + word_85 + ' ' + str(result_85) + '\n')
            except KeyError:
                pass
