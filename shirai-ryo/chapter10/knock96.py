from gensim.models import word2vec
import pickle

model = word2vec.Word2Vec.load('91.model')
country_related_vec = dict()

with open("../chapter09/country.txt") as c_text:
    for line in c_text:
        line = line.strip()
        if not line in model:
            # modelに国名がなかったら
            continue
        country_related_vec[line] = model[line]
    pickle.dump(country_related_vec, open("96.dump", 'wb'))
