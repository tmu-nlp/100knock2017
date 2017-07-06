import pickle
import numpy as np
import knock87
import knock88

if __name__ == '__main__':
    with open('word_context_pca.dump', 'rb') as i_f:
        word_name, pca_matrix = pickle.load(i_f)
    vec_Spa = pca_matrix[word_name['Spain']]
    vec_Mad = pca_matrix[word_name['Madrid']]
    vec_Ath = pca_matrix[word_name['Athens']]
    vec_arg = vec_Spa - vec_Mad + vec_Ath    
    for word, sim in knock88.make_rank(vec_arg, word_name, pca_matrix):
        print ('{}\t{}'.format(word, sim))
