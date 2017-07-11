import numpy
import scipy.stats

data = open('knock94.txt').readlines()

human_sims = []
w2v_sims = []
pca_sims = []

for line in data:
  words = line.strip().split()
  human_sims.append(words[2])
  w2v_sims.append(words[3])
  pca_sims.append(words[4])
human_rank, w2v_rank, pca_rank = numpy.argsort([human_sims, w2v_sims,pca_sims])[::-1]


score = scipy.stats.spearmanr(human_rank, w2v_rank)
score2 = scipy.stats.spearmanr(human_rank,  pca_rank)
print(score.correlation, score2.correlation)
