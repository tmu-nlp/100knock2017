import pickle


if __name__ == "__main__":
  model_fname = './data/w2v_model_knock80.pkl'
  words_fname = './data/family-words_knock91.txt'
  fout = './data/similarity_knock92.txt'

  model = pickle.load(open(model_fname, 'rb'))
  w2v = model.wv
  pairs = list(map(lambda x: x.strip().split(), open(words_fname).readlines()))

  results = list()
  for words in pairs:
    try:
      score = w2v.most_similar(positive=[words[1], words[2]],
                               negative=[words[0]], topn=1)
      results.append("{} {} {:.2f}".format(" ".join(words), *score[0]))
    except:
      continue

  open(fout, 'w').write("\n".join(results))
