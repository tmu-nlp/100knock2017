#!usr/bin/python

import random
import math
import pickle


class logistic_regression:
  def __init__(self, eta):
    self.eta = eta
    self.weights = dict()

  def set_rand_weight(self, key):
    self.weights[key] = random.random()

  def sigmoid(self, z):
    return 1 / (1 + math.exp(-z) )

  def sigma(self, feat_list):
    w_sum = sum(self.weights.get(w, 0) * v for w, v in feat_list)
    return self.sigmoid(w_sum)

  def train(self, t, feat_list):
    prob = self.sigma(feat_list)
    for word, value in feat_list:
      self.weights[word] -= self.eta * (prob - t) * float(value)
    return prob

  def predict(self, feat_list):
    prob = self.sigma(feat_list)
    if prob > 0.5:
      return (1, prob)
    else:
      return (0, prob)


def logistic_train(polarity_file):
  dat = list()
  dat_t = list()
  count = 0
  eta = 0.01 
  print("Prepare features")
  for line in open(polarity_file):
    line = line.strip().split()
    if line[0] == '-1':
      dat_t.append(0)
    else:
      dat_t.append(1)
    feat_list = list()
    for feat in line[1:]:
      name, value = feat.split(':')
      feat_list.append((name, float(value)) )
      logi_reg.set_rand_weight(name)
    dat.append(feat_list)

  print("Start training")
  for ite in range(train_num):
    print("Epoch {}".format(ite), end='\r')
    for num in range(len(dat)):
      logi_reg.train(dat_t[num], dat[num])
    eta *= .5
    logi_reg.eta = eta
  print("done")


if __name__ == "__main__":
    train_num = 50
    polarity_file = 'polarity.dat'
    logi_reg = logistic_regression(0.5)
    logistic_train(polarity_file)
    pickle.dump(logi_reg.weights, open('weight.pkl', 'wb') )
