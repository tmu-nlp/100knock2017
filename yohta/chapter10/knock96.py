from gensim.models import word2vec
import pickle

if __name__ == '__main__':
    model = word2vec.Word2Vec.load('knock90.model')
    country_vec = dict()
    with open('../chapter09/data/country_list.txt') as i_f:
        for line in i_f:
            if not line.strip() in model:
                continue
            country_vec[line.strip()] = model[line.strip()]
    with open('data/knock96.dump', 'wb') as o_f:
        pickle.dump(country_vec, o_f)
