from gensim.models import word2vec
import numpy as np
# from ../chapter09/knock87 import cos_similarity

i_f = word2vec.Text8Corpus('../chapter09/data/answer81.txt')
#model = word2vec.Word2Vec(i_f,size = 300)
#model.save('knock90.model')

if __name__ == '__main__':
    model = word2vec.Word2Vec.load('knock90.model')
    print('knock86')
    print(model['United_States'])
    print('\nknock87')
    print(model.similarity('United_States','U.S'))
#    vec1 = model['United_States']
#    vec2 = model['U.S']
#    print(cos_similarity(vec1,vec2))
    print('\nknock88')
    print(*model.most_similar(positive='England',topn=10))
    print('\nknock89')
#    ans = model['Spain'] - model['Madrid'] + model['Athens']
    print(*model.most_similar(positive=['Spain','Athens'],negative=['Madrid'],topn=10))
