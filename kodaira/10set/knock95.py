import numpy
import scipy.stats

if __name__ == "__main__":
  fname = "./data/similarity_knock94.txt"
  x = numpy.array([list(map(float, line.split())) for line in open(fname)])
  ans, w2v, pca = x.T.argsort(axis=1)
  ans = ans[::-1]
  print("word2vec result: {}\npca      result: {}" \
    .format(*list(map(lambda x: scipy.stats.spearmanr(ans, x), [w2v, pca]))))

