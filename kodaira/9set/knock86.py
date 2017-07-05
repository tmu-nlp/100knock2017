#!usr/bin/python

import pickle

import numpy


def GetVec(mat, vocab):
  def _get_vec(word):
    return mat[vocab.index(word)]
  return _get_vec


if __name__ == "__main__":
  mat = pickle.load(open('./data/pca_mat.pkl', 'rb'))
  vocab = pickle.load(open('./data/vocab.pkl', 'rb'))
  get_vec = GetVec(mat, vocab)

  print(get_vec("United_States"))
