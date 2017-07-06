import pickle
from sklearn.decomposition import TruncatedSVD 
with open('word_context_matrix.dump', 'rb') as i_f:
    word_name, pre_matrix = pickle.load(i_f)
pca = TruncatedSVD(n_components=300)
with open('word_context_pca.dump', 'wb') as o_f:
    pickle.dump((word_name, pca.fit_transform(pre_matrix)), o_f)
