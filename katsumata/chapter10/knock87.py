import pickle
import numpy as np

def cos_sim(v1, v2):
    if (np.linalg.norm(v1)*np.linalg.norm(v2) == 0):
        return 0
    return np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))

if __name__ == '__main__':
    with open('word_context_pca.dump', 'rb') as i_f:
        word_name, pca_matrix = pickle.load(i_f)
    vec_long = pca_matrix[word_name['United_States']]
    vec_short = pca_matrix[word_name['U.S']]
    print ('United_StatesとU.S.の類似度') 
    print ('{}'.format(cos_sim(vec_long, vec_short)))
