from gensim.models import word2vec
import pickle 

if __name__ == '__main__':
    model=word2vec.Word2Vec.load('knock90.emb')
    countries_vec = dict()
    with open('country_list.txt') as country:
        for line in country:
            if not line.strip() in model:
                continue
            countries_vec[line.strip()] = model[line.strip()] 
    with open('country_vec.dump', 'wb') as o_f:
        pickle.dump(countries_vec, o_f)
