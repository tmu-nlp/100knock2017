
import pickle
import numpy as np

def cos_sim(v1, v2):
    if (np.linalg.norm(v1)*np.linalg.norm(v2) == 0):
        return 0
    return np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))

if __name__ == '__main__':
    eng_cos = dict()
    with open('word_context_pca.dump', 'rb') as i_f:
        word_name, pca_matrix = pickle.load(i_f)

    vec_Eng = pca_matrix[word_name['England']]
    for word in word_name:
        if word == 'England':
            continue
        vec = pca[word_name[word]]
        sim = cos_sim(vec_Eng, vec)
        eng_cos[word] = sim

    count = 0
    for k, v in sorted(eng_cos.items(), key = lambda x:x[1], reverse = True):
        count += 1
        print(count, k, v)
        if count == 10:
            break
