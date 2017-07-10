from gensim.models import word2vec
from scipy import spatial
from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    corpus = word2vec.Text8Corpus('../chapter09/corpus_81.txt')
    model = word2vec.Word2Vec(corpus,size=300)
    model.save('knock90.model')
    print('knock86')
    print(model['United_States'])
    print()
    print('knock87')
    print(1-spatial.distance.cosine(model['United_States'],model['U.S']))
    print()
    print('knock88')
    result = model.most_similar(positive=['England'])
    i = 0
    for r in result:
        print(r)
        i += 1
        if i == 10:
            break
    print()
    print('knock89')
    vec = (np.array(model['Spain']) - np.array(model['Madrid']) + np.array(model['Athens'])).tolist()
    result = model.most_similar(positive=['Spain','Athens'], negative=['Madrid'])
    i = 0
    for r in result:
        print(r)
        i += 1
        if i >= 10:
            break

