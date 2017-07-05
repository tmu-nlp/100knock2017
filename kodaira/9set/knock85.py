#!usr/bin/python

import pickle

import sklearn.decomposition 
import numpy


dim = 100

print("Load ppmi_matrix")
mat = pickle.load(open('./data/ppmi_mat.pkl', 'rb')).todense()

pca = sklearn.decomposition.PCA(dim, copy=False)

print("pca")
mat = pca.fit_transform(mat)

print("ouput shape: ", mat.shape)
print("save result", flush=True, end=" ")
pickle.dump(mat, open('./data/pca_mat.pkl', 'wb'))
print("done")
