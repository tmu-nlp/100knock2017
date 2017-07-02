#!usr/bin/python

import pickle

import numpy

from knock86 import GetVec


def cos(vec, mat):
  return numpy.dot(mat, vec) / \
    (numpy.linalg.norm(vec) * numpy.linalg.norm(mat, axis=1))


if __name__ == '__main__':
  mat = pickle.load(open('./data/pca_mat.pkl', 'rb'))
  vocab = pickle.load(open('./data/vocab.pkl', 'rb'))
  get_vec = GetVec(mat, vocab)

  x = get_vec('United_States')
  y = get_vec('U.S')

  print(cos(x, y.reshape(1, y.size)))
