#!usr/bin/python

import pickle

import numpy

from knock87 import GetVec
from knock88 import cos


if __name__ == '__main__':
  mat = pickle.load(open('./data/pca_mat.pkl', 'rb'))
  vocab = pickle.load(open('./data/vocab.pkl', 'rb'))
  get_vec = GetVec(mat, vocab)

  vector = get_vec('Spain') - get_vec('Madrid') + get_vec('Athens')

  cos_vec = cos(vector, mat)
  ids = cos_vec.argsort()

  for rank, i in enumerate(ids[-2:-12:-1]):
    print("Rank{:2d}\t{:10s}\t{:.4f}".format(rank, vocab[i], cos_vec[i]))
