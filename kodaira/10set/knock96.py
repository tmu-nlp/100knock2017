import pickle


if __name__ == "__main__":
  model_fname = "./data/w2v_model_knock80.pkl"
  country_fname = "../9set/data/country.txt"
  fout = "./data/country2vec_knock96.pkl"

  model = pickle.load(open(model_fname, 'rb'))
  countrys = [line.strip().replace(" ", "_") for line in open(country_fname)]

  c2v = dict()
  for country in countrys:
    if country in model.wv:
      c2v[country] = model.wv[country]

  pickle.dump(c2v, open(fout, 'wb'))
