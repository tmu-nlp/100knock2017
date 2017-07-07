import pickle

with open('word_context_pca.dump', 'rb') as i_f:
    word_name, pca_matrix = pickle.load(i_f)
print (pca_matrix[word_name['United_States']])
