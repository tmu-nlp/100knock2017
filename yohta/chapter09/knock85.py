import pickle
from sklearn.decomposition import TruncatedSVD

with open('data/answer84','rb') as i_f:
    words,vector = pickle.load(i_f)

trunc = TruncatedSVD(n_components = 300)
with open('data/answer85','wb') as o_f:
    pickle.dump((words,trunc.fit_transform(vector)),o_f)
