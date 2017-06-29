#coding: utf-8


import matplotlib.pyplot as plt
import matplotlib.pyplot as np

def draw_graph(result):
  acc_list = list() ; rec_list = list()
  
  plt.plot(result[0], result[1])
  plt.xlim(0., 1.)
  plt.ylim(0., 1.)
  plt.title('precision - recall')
  plt.xlabel('precision')
  plt.ylabel('recall')
  plt.show()
  

def get_rec_pre(result):

  results = list()
  for line in result:
    ans, pred, prob = map(float, line.split("\t"))
    results.append((ans, pred, prob))
  ans, pred, _ = zip(*sorted(results, key=lambda x: -x[2]))
  tp, fp, fn = 0, 0, 0
  recs, pres = list(), list()
  pre_denom = sum(ans)
  for a in ans:
    if a ==1.0:
      tp += 1
    elif a == 0:
      fp += 1
    if (tp + fn) != 0:
      pres.append(tp / (tp + fp))
      recs.append(tp / pre_denom)
  print(recs)

  return pres, recs


if __name__ == '__main__':
  import sys

  result = open(sys.argv[1], 'r')
  result = get_rec_pre(result)
  draw_graph(result)
