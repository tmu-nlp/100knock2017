#!usr/bin/python

import pickle

import numpy

from knock86 import GetVec
from knock87 import cos


if __name__ == '__main__':
  mat = pickle.load(open('./data/pca_mat.pkl', 'rb'))
  vocab = pickle.load(open('./data/vocab.pkl', 'rb') )
  get_vec = GetVec(mat, vocab)

  cos_list = list()

  england_vec = get_vec("England")

  cos_vec = cos(england_vec, mat)

  ids = cos_vec.argsort()

  for rank, i in enumerate(ids[-2:-12:-1]):
    print("Rank{:2d}\t{:10s}\t{:.4f}".format(rank, vocab[i], cos_vec[i]))
