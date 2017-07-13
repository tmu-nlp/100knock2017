from gensim.models import word2vec
import pickle
from scipy import spatial
from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    model = word2vec.Word2Vec.load('knock90.model')
    country_list = pickle.load(open('all_country.pickle','rb'))

    country_model = defaultdict(list)
    for country in country_list:
        if country in model:
            country_model[country] = model[country]
    print(len(country_model))
    pickle.dump(country_model,open('country_model.pickle','wb'))
