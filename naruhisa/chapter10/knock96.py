from gensim.models import word2vec
import pickle

if __name__ == '__main__':
    with open('../chapter09/countries.txt', 'r') as i_f, open('c_vec.pkl', 'wb') as o_f:
        c_dict = dict()
        model = word2vec.Word2Vec.load('model.w2v')
        for line in i_f:
            line = '_'.join(line.strip().split())
            try:
                c_dict[line] =  model[line]
            except KeyError:
                print('{} is not in vocabulary' .format(line))

        pickle.dump(c_dict, o_f)
